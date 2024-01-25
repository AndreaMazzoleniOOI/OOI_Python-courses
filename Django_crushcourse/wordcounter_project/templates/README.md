## Spiegazione codice html

1. *{% load static %}* load tag static into Django
2. *link* link the html file to the static file css. If a file is static it must be enclosed in
    *{%static 'staticfilename' %}*
3. *action=counter* posts the value in the *form* to the page *counter* 
4. Method *POST* will not show the *text* in the link of the webpage. This will require a *CSRF token* that must be added

```html
{% load static %}

<link rel="stylesheet" href="{%static 'style.css'' %}">

<h1>Input your text below</h1>

<form method="POST" action="counter">
  {% csrf_token %}
  <textarea name="text" rows="25" cols="100"> </textarea><br>
  <input type="submit"/>
</form>
```