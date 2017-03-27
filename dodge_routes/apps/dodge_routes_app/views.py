from django.shortcuts import render

def index(request):
	return render(request, 'dodge_routes_app/index.html')

# def all(request):
# 	context = {
# 		'image':'dodge_routes_app/images/dodge-all.jpg'
# 	}
# 	return render(request, 'dodge_routes_app/all.html', context)

def show(request, car):
	cars = {
		'challenger':'dodge_routes_app/images/challenger.jpg',
		'charger':'dodge_routes_app/images/charger.jpg',
		'caravan':'dodge_routes_app/images/caravan.jpg',
		'dart':'dodge_routes_app/images/dart.jpg',
		'durango':'dodge_routes_app/images/durango.jpg',
		'journey':'dodge_routes_app/images/journey.jpg',
		'all':'dodge_routes_app/images/dodge-all.jpg'
	}
	if car in cars:
		context = {
			'image':cars[car]
		}
	else:
		context = {
			'image':'dodge_routes_app/images/demon.jpg'
		}
	return render(request, 'dodge_routes_app/show.html', context)