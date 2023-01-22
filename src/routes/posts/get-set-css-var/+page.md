How to get and set CSS variables
================================

Get:

```coffeescript
element = document.getElementById('myid')
color = getComputedStyle(element).getPropertyValue('--bg-color')
```

Set:

```coffeescript
element = document.getElementById('myid')
element.style.setProperty('--bg-color', '#999999')
```
