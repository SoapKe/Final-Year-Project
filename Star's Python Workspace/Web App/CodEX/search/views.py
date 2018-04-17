# coding:utf-8
# @author: Star
# @time: 10-03-2018
import search.supportings.FCIConverter as fci
from django.shortcuts import render
from django.http import HttpResponse
from search.supportings.LSI.LSI_TFIDF import LSI_TFIDF
import CodEX.config as config
from search.supportings.FrontEndInterface import FrontEndInterface


def index(request):
    return render(request, 'index-sub.html')


def search(request):
    q = request.GET['q']
    p = int(request.GET['p'])
    pages = []
    lsi = LSI_TFIDF()
    result = lsi.getDocumentList(query=q, page=p)
    f = result.getDocumentList()
    total_p = (result.getNumOfResults() / 10) + 1;
    t_p = int(total_p)
    p_p = max(p - 5, 1)
    n_p = min(p + 5, total_p)
    while total_p > 0:
        pages.append(0)
        total_p -= 1
    files = []
    for f_f in f:
        f_name = f_f[0]
        temp = fci.to_fciObject(config.configs['paths']['FCI_path'] + "/" + f_name)
        m_l = ''
        for t_f_f in f_f[1]:
            m_l += str(t_f_f + 1)
            m_l += ','
        m_l = m_l[0:len(m_l) - 1]
        fei = FrontEndInterface(temp, m_l)
        files.append(fei)
    return render(request, 'search-result-sub.html',
                  {'results': files, 'q': q, 'p': p, 'pages': pages, 'p_p': p_p, 'n_p': n_p, 'pre': p - 1,
                   'next': p + 1, 't_p': t_p})


def init(request):
    LSI_TFIDF().indexing()
    return HttpResponse("init successfully")


def plagiarize(request):

    return render(request, 'snippet.html', {})


def plagiarizeResult(request):
    snippet = request.GET['snippet']
    return render(request, 'snippet-result.html', {'snippet':snippet})


def detail(request):
    id = request.GET['id']
    ml = request.GET['ml']
    m_l = ml
    fci_obj = fci.to_fciObject(config.configs['paths']['FCI_path'] + "/" + id + '.json')
    return render(request, 'detail-sub.html', {'detail': fci_obj, 'match_lines': m_l})
