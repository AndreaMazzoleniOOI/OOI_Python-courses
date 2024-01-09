## Spiegazione codice html

1. *action=counter* posts the value in the *form* to the page *counter* 
2. Method *POST* will not show the *text* in the link of the webpage. This will require a *CSRF token* that must be added

```html
<h1>Input your text below</h1>

<form method="POST" action="counter">
  <textarea name="text" rows="25" cols="100"> </textarea><br>
  <input type="submit"/>
</form>
```