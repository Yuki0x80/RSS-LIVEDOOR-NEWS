from django.shortcuts import render

# Create your views here.
# coding: utf-8
from django.http import HttpResponse
from django.conf import settings
from django.utils.xmlutils import SimplerXMLGenerator
from xml.dom import minidom
import feedparser
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import urllib2
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
	return render_to_response('index.html')

def top(request):
	#t = get_template('test.html')
	req = urllib2.Request("http://news.livedoor.com/topics/rss/top.xml")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())
	

def dom(request):
	req = urllib2.Request("http://news.livedoor.com/topics/rss/dom.xml ")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())

def inter(request):
	req = urllib2.Request("http://news.livedoor.com/topics/rss/int.xml")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())

def eco(request):
	req = urllib2.Request("http://news.livedoor.com/topics/rss/eco.xml ")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())

def ent(request):
	req = urllib2.Request("http://news.livedoor.com/topics/rss/ent.xml ")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())

def spo(request):
	req = urllib2.Request("http://news.livedoor.com/topics/rss/spo.xml ")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())

def movie(request):
	req = urllib2.Request("http://news.livedoor.com/rss/summary/52.xml ")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())

def gourmet(request):
	req = urllib2.Request("http://news.livedoor.com/topics/rss/gourmet.xml")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())

def love(request):
	req = urllib2.Request("http://news.livedoor.com/topics/rss/love.xml ")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())

def trend(request):
	req = urllib2.Request("http://news.livedoor.com/topics/rss/trend.xml ")
	opener = urllib2.build_opener()
	doc = minidom.parse(opener.open(req))
	return HttpResponse(doc.toxml())