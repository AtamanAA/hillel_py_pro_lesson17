from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Student
from .forms import StudentForm


def all_students(request):
    students_list = list(Student.objects.all().order_by("id").values())
    return render(
        request, "student/all_students.html", {"students_list": students_list}
    )


def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Form isn't valid. Try again!")
            return HttpResponseRedirect(reverse("create_student"))
        form.save()
        messages.success(request, "New student create successful!")
        return HttpResponseRedirect(reverse("all_students"))
    else:
        form = StudentForm()
    return render(request, "student/create.html", {"form": form})


def edit_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        messages.error(
            request, f"Student with ID: {student_id} doesn't exist. Try another ID!"
        )
        return HttpResponseRedirect(reverse("all_students"))
    if request.method == "POST":
        if "edit" in request.POST:
            form = StudentForm(request.POST, instance=student)
            if not form.is_valid():
                messages.error(request, "Form isn't valid. Try again!")
                return HttpResponseRedirect(
                    reverse("edit_student", args=[form.instance.id])
                )

            groups = list(form.cleaned_data["group"])
            student.group.clear()
            for group in groups:
                student.group.add(group)

            form.save()
            messages.success(
                request, f"Student with ID {student_id} update successful!"
            )
            return HttpResponseRedirect(reverse("all_students"))
        elif "delete" in request.POST:
            student.delete()
            messages.success(request, f"Student with ID {student_id} delete!")
            return redirect("all_students")
    else:
        initial_groups = [group.id for group in student.group.all()]
        form = StudentForm(instance=student, initial={"group": initial_groups})
        return render(request, "student/edit.html", {"form": form})
