Parcel
======

https://parceljs.org/features/development/

```bash
$ mkdir webapp
$ cd webapp
$ mkdir src
$ npm init -y
$ git init
$ npm install -g parcel
```

Create an HTML file at `src/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8"/>
		<title>My First Parcel App</title>
	</head>
	<body>
		<h1>Hello, World!</h1>
	</body>
</html>
```

Start the web server with:

```bash
$ parcel serve src/index.html --open
```

