from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Teacher, Subject
from .forms import TeacherForm, SubjectForm


def all_teachers(request):
    teachers_list = []
    for person in Teacher.objects.all().order_by("id"):
        result = {
            "id": person.id,
            "first_name": person.first_name,
            "last_name": person.last_name,
            "patronymic": person.patronymic,
            "birthday": person.birthday,
            "subject": person.subject.name,
        }
        teachers_list.append(result)
    return render(request, "teacher/all_teachers.html", {"teachers_list": teachers_list})


def create_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Form isn't valid. Try again!")
            return HttpResponseRedirect(reverse("create_teacher"))
        form.save()
        messages.success(request, "New teacher create successful!")
        return HttpResponseRedirect(reverse("all_teachers"))
    else:
        form = TeacherForm()
    return render(request, "teacher/create.html", {"form": form})


def edit_teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
    except Teacher.DoesNotExist:
        messages.error(request, f"Teacher with ID: {teacher_id} doesn't exist. Try another ID!")
        return HttpResponseRedirect(reverse("all_teachers"))
    if request.method == "POST":
        if "edit" in request.POST:
            form = TeacherForm(request.POST, instance=teacher)
            if not form.is_valid():
                messages.error(request, "Form isn't valid. Try again!")
                return HttpResponseRedirect(reverse("edit_teacher", args=[form.instance.id]))
            form.save()
            messages.success(request, f"Teacher with ID {teacher_id} update successful!")
            return HttpResponseRedirect(reverse("all_teachers"))
        elif "delete" in request.POST:
            teacher.delete()
            messages.success(request, f"Teacher with ID {teacher_id} delete!")
            return redirect("all_teachers")
    else:
        form = TeacherForm(instance=teacher)
        return render(request, "teacher/edit.html", {"form": form})


def all_subjects(request):
    subjects_list = list(Subject.objects.all().order_by("id").values())
    return render(request, "teacher/all_subjects.html", {"subjects_list": subjects_list})


def create_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Form isn't valid. Try again!")
            return HttpResponseRedirect(reverse("create_subject"))
        form.save()
        messages.success(request, "New subject create successful!")
        return HttpResponseRedirect(reverse("all_subjects"))
    else:
        form = SubjectForm()
    return render(request, "teacher/create_subject.html", {"form": form})


def edit_subject(request, subject_id):
    try:
        subject = Subject.objects.get(pk=subject_id)
    except Subject.DoesNotExist:
        messages.error(request, f"Teacher with ID: {subject_id} doesn't exist. Try another ID!")
        return HttpResponseRedirect(reverse("all_subjects"))
    if request.method == "POST":
        if "edit" in request.POST:
            form = SubjectForm(request.POST, instance=subject)
            if not form.is_valid():
                messages.error(request, "Form isn't valid. Try again!")
                return HttpResponseRedirect(reverse("edit_subject", args=[form.instance.id]))
            form.save()
            messages.success(request, f"Subject with ID {subject_id} update successful!")
            return HttpResponseRedirect(reverse("all_subjects"))
        elif "delete" in request.POST:
            subject.delete()
            messages.success(request, f"Subject with ID {subject_id} delete!")
            return redirect("all_subjects")
    else:
        form = SubjectForm(instance=subject)
        return render(request, "teacher/edit_subject.html", {"form": form})
