from calendar import Calendar
from datetime import datetime

from django.shortcuts import render, redirect
from django.utils import timezone

from config import Paginator
from config.utils.datetime import add_months
from .models import MinaPost


def post(request, pk=None, page_number=None):
    post_list = MinaPost.objects.order_by('created_date')
    paginator = Paginator(post_list, 1, adjacent_pages=3)

    try:
        if page_number:
            posts = paginator.page(page_number)
            post = posts.object_list[0]
            return redirect('mina:post', pk=post.pk)
        else:
            post = MinaPost.objects.get(pk=pk)
    except MinaPost.DoesNotExist:
        post = post_list.last()
        return redirect('mina:post', pk=post.pk)

    page_index = MinaPost.objects.get_index(post, compare_field='created_date',
                                            sort='ascending') + 1
    posts = paginator.page(page_index)

    now = timezone.make_aware(datetime.now())
    try:
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        cal_date = timezone.make_aware(datetime(year, month, 1))
    except:
        year = post.created_date.year
        month = post.created_date.month
        cal_date = post.created_date

    cal = Calendar()
    month_days = cal.itermonthdays(year, month)
    week_list = [[]]
    week = 0
    for day in month_days:
        day_posts = []
        if day:
            day_posts = MinaPost.objects.filter(
                created_date__year=year,
                created_date__month=month,
                created_date__day=day,
            )
        dp_id_list = [post.id for post in day_posts]
        posts_id_list = [post.id for post in posts]
        day_info = {
            'day': day,
            'posts': day_posts,
            'today': True if now.year == year and now.month == month and now.day == day else False,
            'current': True if dp_id_list == posts_id_list else False,
        }
        week_list[week].append(day_info)
        if len(week_list[week]) == 7:
            week_list.append([])
            week += 1

    context = {
        'posts': posts,
        'week_list': week_list,
        'year': year,
        'month': month,
        'cal_prev_date': add_months(cal_date, -1),
        'cal_next_date': add_months(cal_date, +1),
    }
    return render(request, 'mina/post.html', context)
