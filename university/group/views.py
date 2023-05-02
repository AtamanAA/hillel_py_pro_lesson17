from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Group
from .forms import GroupForm, StudentToGroupForm


def all_groups(request):
    groups_list = []
    for group in Group.objects.all().order_by("id"):
        result = {
            "id": group.id,
            "name": group.name,
            "teacher": group.teacher,
            "students_count": len(group.students.all()),
        }
        groups_list.append(result)
    return render(request, "group/all_groups.html", {"groups_list": groups_list})


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Form isn't valid. Try again!")
            return HttpResponseRedirect(reverse("create_group"))
        form.save()
        messages.success(request, "New group create successful!")
        return HttpResponseRedirect(reverse("all_groups"))
    else:
        form = GroupForm()
    return render(request, "group/create.html", {"form": form})


def edit_group(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
    except Group.DoesNotExist:
        messages.error(
            request, f"Group with ID: {group_id} doesn't exist. Try another ID!"
        )
        return HttpResponseRedirect(reverse("all_groups"))
    if request.method == "POST":
        if "edit" in request.POST:
            form = GroupForm(request.POST, instance=group)
            if not form.is_valid():
                messages.error(request, "Form isn't valid. Try again!")
                return HttpResponseRedirect(
                    reverse("edit_group", args=[form.instance.id])
                )
            form.save()
            messages.success(request, f"Group with ID {group_id} update successful!")
            return HttpResponseRedirect(reverse("all_groups"))
        elif "delete" in request.POST:
            group.delete()
            messages.success(request, f"Group with ID {group_id} delete!")
            return redirect("all_groups")
    else:
        form = GroupForm(instance=group)
        return render(request, "group/edit.html", {"form": form})


def student_to_group(request):
    if request.method == "POST":
        if "refresh" in request.POST:
            initial_group = request.POST["group"]
            group = Group.objects.get(pk=initial_group)
            initial_students = list(group.students.all())
            form = StudentToGroupForm(
                initial={"group": initial_group, "students": initial_students}
            )
            return render(request, "group/student_to_group.html", {"form": form})

        elif "update" in request.POST:
            form = StudentToGroupForm(request.POST)
            if not form.is_valid():
                messages.error(request, "Form isn't valid. Try again!")
                return HttpResponseRedirect(reverse("student_to_group"))

            # Add student to groups
            group = form.cleaned_data["group"]
            students = list(form.cleaned_data["students"])
            group.students.clear()
            for student in students:
                student.group.add(group)

            messages.success(request, "Student add to group successful!")
            return HttpResponseRedirect(reverse("all_groups"))
    else:
        form = StudentToGroupForm()
        return render(request, "group/student_to_group.html", {"form": form})
