# coding: utf8

def message():
	msg = ("Hello everybody, today I'm learning how to create functions in python")
	print(msg)

message()

def favorite_book(title):
	msg = "One of my favorite books is "
	print(msg + title.title())

favorite_book('les brillant - marcus sakhé')