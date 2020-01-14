from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from . import forms


class HomeView(ListView):

    """ HomeView Views Definition """

    model = models.Room
    paginate_by = 10
    page_kwarg = "page"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Views Definition """

    model = models.Room


class SearchView(View):

    """ SearchView Deifinition """

    def get(self, request):

        country = request.GET.get("country")
        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__lte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__lte"] = bedrooms

                if beds is not None:
                    filter_args["beds__lte"] = beds

                if baths is not None:
                    filter_args["baths__lte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = instant_book

                if superhost is True:
                    filter_args["host__superhost"] = superhost

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")
                paginator = Paginator(qs, 10)
                page = request.GET.get("page", 1)
                rooms = paginator.get_page(page)
                return render(
                    request, "rooms/search.html", {"form": form, "rooms": rooms}
                )

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form})


# def search(request):

#     country = request.GET.get("country")
#     if country:
#         form = forms.SearchForm(request.GET)
#         if form.is_valid():
#             city = form.cleaned_data.get("city")
#             country = form.cleaned_data.get("country")
#             room_type = form.cleaned_data.get("room_type")
#             price = form.cleaned_data.get("price")
#             guests = form.cleaned_data.get("guests")
#             bedrooms = form.cleaned_data.get("bedrooms")
#             beds = form.cleaned_data.get("beds")
#             baths = form.cleaned_data.get("baths")
#             instant_book = form.cleaned_data.get("instant_book")
#             superhost = form.cleaned_data.get("superhost")
#             amenities = form.cleaned_data.get("amenities")
#             facilities = form.cleaned_data.get("facilities")

#             filter_args = {}

#             if city != "Anywhere":
#                 filter_args["city__startswith"] = city

#             filter_args["country"] = country

#             if room_type is not None:
#                 filter_args["room_type"] = room_type

#             if price is not None:
#                 filter_args["price__lte"] = price

#             if guests is not None:
#                 filter_args["guests__lte"] = guests

#             if bedrooms is not None:
#                 filter_args["bedrooms__lte"] = bedrooms

#             if beds is not None:
#                 filter_args["beds__lte"] = beds

#             if baths is not None:
#                 filter_args["baths__lte"] = baths

#             if instant_book is True:
#                 filter_args["instant_book"] = instant_book

#             if superhost is True:
#                 filter_args["host__superhost"] = superhost

#             for amenity in amenities:
#                 filter_args["amenities"] = amenity

#             for facility in facilities:
#                 filter_args["facilities"] = facility

#             print(filter_args)
#             rooms = models.Room.objects.filter(**filter_args)
#             return render(request, "rooms/search.html", {"form": form, "rooms": rooms})

#     else:
#         form = forms.SearchForm()
#         return render(request, "rooms/search.html", {"form": form})


# form = {
#     "city": city,
#     "s_country": country,
#     "s_room_type": room_type,
#     "price": price,
#     "guests": guests,
#     "bedrooms": bedrooms,
#     "beds": beds,
#     "baths": baths,
#     "s_amenities": s_amenities,
#     "s_facilities": s_facilities,
#     "instant": instant,
#     "superhost": superhost,
# }

# room_types = models.RoomType.objects.all()
# amenities = models.Amenity.objects.all()
# facilities = models.Facility.objects.all()

# choices = {
#     "countries": countries,
#     "room_types": room_types,
#     "amenities": amenities,
#     "facilities": facilities,
# }

# return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms},)


# from django.shortcuts import render, redirect, reverse
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         return redirect(reverse("core:home"))
