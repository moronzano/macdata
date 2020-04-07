from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Switches, DhcpTable, StoreMac, MacDhcp
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, "switches/index.html")


class SwithesView(View):
    # Тоже альтернатива
    def get(self, request):
        switches = Switches.objects.all()
        return render(request, "switches/switch_list.html", {"switch_list": switches})


class SwithesView2(ListView):

    model = Switches
    context_object_name = "switch_list"
    template_name = "switches/switch_list.html"
    paginate_by = 20

    # Оставлено в качестве альтернативного примера пагинации
    # def get_queryset(self):
    #    queryset = Switches.objects.all().order_by("ip_switch")
    #    # Отбираем первые 10 статей
    #    paginator = Paginator(queryset, 20)
    #    page = self.request.GET.get('page')
    #    try:
    #        queryset = paginator.page(page)
    #    except PageNotAnInteger:
    #        # If page is not an integer, deliver first page.
    #        queryset = paginator.page(1)
    #    except EmptyPage:
    #        # If page is out of range (e.g. 9999), deliver last page of results.
    #        queryset = paginator.page(paginator.num_pages)
    #    return queryset


class DhcpView(ListView):

    model = DhcpTable
    context_object_name = "dhcp_list"
    template_name = "switches/dhcp_list.html"
    paginate_by = 20


class StoreMacView(ListView):
    model = StoreMac
    context_object_name = "storemac_list"
    template_name = "switches/storemac_list.html"
    paginate_by = 20


class StoreMacFilterView(ListView):
    model = StoreMac
    context_object_name = "storemac1_list"
    template_name = "switches/storemacfilter_list.html"
    paginate_by = 20

    def get_queryset(self):
        search_query = self.request.GET.get('search_1', '')
        # if search_query:
        #    queryset = StoreMac.objects.all().filter(
        #        Q(ip_switch__ip_switch=search_query) | Q(mac=search_query) | Q(vlan=search_query))
        # else:
        #    queryset = StoreMac.objects.all().order_by("ip_switch")
        queryset = StoreMac.objects.all().filter(
            Q(ip_switch__ip_switch=search_query) | Q(mac=search_query) | Q(vlan=search_query))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search_1"] = ''.join(
            [f"search_1={x}&" for x in self.request.GET.getlist("search_1")])
        return context


class MacDhcpView(ListView):
    model = MacDhcp
    context_object_name = "macdhcp_list"
    template_name = "switches/macdhcp_list.html"
    paginate_by = 20

    def get_queryset(self):
        queryset = MacDhcp.objects.Mac_to_Dhcp()
        return queryset


class SwithesDetail(ListView):
    model = Switches
    context_object_name = "sw1_list"
    template_name = "switches/sw1.html"
    # paginate_by = 20

    def get(self, request):
        queryset = Switches.objects.all()
        paginator = Paginator(queryset, 20)
        page = request.GET.get('page2')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        pn2 = page
        content = {"sw1_list": queryset, "pn2": pn2}
        #content = {"sw1_list": queryset}
        return render(request, "switches/sw1.html", content)


class StoreMacView2(ListView):
    model = StoreMac
    context_object_name = "sw1_detail"
    template_name = "switches/sw1_detail.html"
    # paginate_by = 20

    def get(self, request, pk1, p1):
        switches = Switches.objects.all()
        # print(pk1)
        queryset = StoreMac.objects.all().filter(ip_switch=pk1)
        paginator = Paginator(queryset, 20)
        page = request.GET.get('page')
        paginator2 = Paginator(switches, 20)
        page2 = request.GET.get('page2')
        print(p1)
        # print(page2)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        try:
            switches = paginator2.page(page2)
        except PageNotAnInteger:
            page2 = p1
            switches = paginator2.page(page2)
        except EmptyPage:
            switches = paginator2.page(paginator.num_pages)
        pn = page
        pn2 = page2
        content = {"sw1_list": switches,
                   "sw1_detail": queryset, "pn2": pn2, "pn": pn}

        return render(request, "switches/sw1_detail.html", content)

    # def get_queryset(self):
    #    id_ = self.kwargs['pk1']
    #    switches = Switches.objects.all()
    #    queryset = StoreMac.objects.filter(ip_switch=id_)
    #    content = {"sw1_list": switches, "sw1_detail": queryset}
    #    return render(self.request, "switches/sw1_detail.html", content)
