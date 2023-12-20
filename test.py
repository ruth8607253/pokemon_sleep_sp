<!DOCTYPE html>
<html>
<head>
    <title>輪播廣告</title>
</head>
<body>
<nav>
    <div id="PIC">
        <ul>
            {% for _ in range(10) %}
                <li><img src="{{ url_for('static', filename='img/display/') | random_image }}" width="800" height="200" alt=""></li>
            {% endfor %}
        </ul>
    </div>
</nav>
</body>
</html>
