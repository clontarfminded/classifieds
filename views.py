from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Classified, Page, Locale, Section, Subsection, Province, Region
from .forms import CreateClassifiedForm

def index(request):
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'page_list': page_list,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/index.html', context)

def locale_index(request, locale_id):
    l = get_object_or_404(Locale, pk=locale_id)
    r = get_object_or_404(Region, pk=l.region_id)
    p = get_object_or_404(Province, pk=l.province_id)
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'locale': l,
        'region': r,
        'province': p,
        'page_list': page_list,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/locale-index.html', context)

def section_index(request, locale_id, section):
    l = get_object_or_404(Locale, pk=locale_id)
    s = get_object_or_404(Section, section_name=section)
    section_classified_list = Classified.objects.filter(locale_id=locale_id).filter(section__section_name=section).order_by('datetime_created')
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'locale': l,
        'section': section,
        'page_list': page_list,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'section_classified_list': section_classified_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/section-index.html', context)

def subsection_index(request, locale_id, section, subsection):
    l = get_object_or_404(Locale, pk=locale_id)
    s = get_object_or_404(Section, section_name=section)
    ss = get_object_or_404(Subsection, subsection_name=subsection)
    subsection_classified_list = Classified.objects.filter(locale_id=locale_id).filter(section__section_name=section).filter(subsection__subsection_name=subsection).order_by('datetime_created')
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'page_list': page_list,
        'locale': l,
        'section': s,
        'subsection': ss,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'subsection_classified_list': subsection_classified_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/subsection-index.html', context)

def detail(request, classified_id):
    classified = get_object_or_404(Classified, pk=classified_id)
    l = get_object_or_404(Locale, pk=classified.locale_id)
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'classified': classified,
        'locale': l,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/detail.html', context)

def region(request, region_id):
    r = get_object_or_404(Region, pk=region_id)
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    province_list_sorted = Province.objects.filter(region_id=region_id).order_by('province_name')
    region_list = Region.objects.order_by('pk')
    context = {
        'region': r,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
        'province_list_sorted': province_list_sorted,
    }
    return render(request, 'classifieds/region-index.html', context)

def province(request, province_id):
    p = get_object_or_404(Province, pk=province_id)
    locale_list = Locale.objects.order_by('locale_name')
    locale_list_sorted = Locale.objects.filter(province_id=province_id).order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'province': p,
        'region': p.region,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
        'locale_list_sorted': locale_list_sorted
    }
    return render(request, 'classifieds/province-index.html', context)

def page(request, page_name):
    page = get_object_or_404(Page, page_name=page_name)
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'page': page,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/page.html', context)

def thanks(request):
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/thanks.html', context)

def create_classified(request):
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    if request.method == 'POST':
        form = CreateClassifiedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = CreateClassifiedForm().as_ul()
        context = {
            'form': form,
            'locale_list': locale_list,
            'section_list': section_list,
            'subsection_list': subsection_list,
            'page_list': page_list,
            'province_list': province_list,
            'region_list': region_list,
        }
    return render(request, 'classifieds/create-classified.html', context)
