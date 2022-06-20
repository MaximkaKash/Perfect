from django.urls import path
from ferumbel.views import ProductsView, product_details_view, register_view, Contact, AboutUs, page_not_found_view, \
    logout_user, activeOrder_view, confirmedOrder_view, deletedOrder_view, \
    basket, autorization, activeOrders, confirmedOrders, deletedOrders, ProductsView1, transport_index_to_topycs, category_view, sitemap ,Index, get_file
from django.conf import settings

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contacts/', Contact.as_view(), name='contacts'),
    path("register/", register_view, name="register_view"),
    path('aboutUs/', AboutUs.as_view(), name='aboutUs'),
    path("catalog/", ProductsView.as_view(), name="products_view"),
    path("catalog1/", ProductsView1.as_view(), name="products_view1"),
    path(
        "product/<int:product_id>/", product_details_view, name="product_details_view"
    ),
    path("category/<int:category_id>/", category_view, name="category_view"),
    path("basket/", basket, name="basket"),
    path(
         "catalog2/<int:product_id>/", transport_index_to_topycs, name="transport_index_to_topycs"
         ),

    path("autorization/", autorization, name="autorization"),
    path("activeOrders/", activeOrders, name="activeOrders"),
    path(
        "activeOrder/<int:order_index>/", activeOrder_view, name="activeOrder_view"
    ),
    path("confirmedOrders/", confirmedOrders, name="confirmedOrders"),
    path(
        "confirmedOrder/<int:order_index>/", confirmedOrder_view, name="confirmedOrder_view"
    ),
    path("deletedOrders/", deletedOrders, name="deletedOrders"),
    path(
        "deletedOrder/<int:order_index>/", deletedOrder_view, name="deletedOrder_view"
    ),
    path("logout/", logout_user, name='logout'),
    path("sitemap", sitemap, name="sitemap"),
    path("file/", get_file, name='get_file'),
]

handler404 = page_not_found_view