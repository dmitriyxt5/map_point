from django.shortcuts import render
from map_points.models import MapPoint
from django.shortcuts import render, redirect
from .forms import MapPointForm



from django.shortcuts import render
from .models import MapPoint

def home(request):
    # 1. Убираем статус и сортируем: самые новые — вверху
    # 2. Берем только последние 20 записей через срез [:20]
    # Django выполнит это на уровне SQL (LIMIT 20)
    points = MapPoint.objects.all().order_by('-created_at')[:20]

    geojson_points = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "title": p.title,
                    "description": p.description,
                    # Проверка на наличие фото, чтобы не упасть с ошибкой
                    "image": p.image.url if p.image else None,
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(p.longitude), float(p.latitude)],
                },
            }
            for p in points
        ],
    }

    return render(
        request,
        "map_points/home.html",
        {
            "geojson_points": geojson_points,
        },
    )


def add_point(request):
    if request.method == 'POST':
        form = MapPointForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()  
            return redirect('point_success')
    else:
        form = MapPointForm()

    return render(
        request,
        'map_points/add_point.html',
        {'form': form}
    )


def point_success(request):
    return render(request, 'map_points/point_success.html')