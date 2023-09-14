<!DOCTYPE html>
<html>
<head>
    <title>Django REST API Documentation</title>
</head>
<body>

<h1>Django REST API Documentation</h1>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#setup">Setup</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#api-endpoints">API Endpoints</a></li>
    <li><a href="#sample-requests-and-responses">Sample Requests and Responses</a></li>
    <li><a href="#known-limitations-and-assumptions">Known Limitations and Assumptions</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2 id="introduction">Introduction</h2>
<p>This Django REST API provides CRUD (Create, Read, Update, Delete) operations for managing persons. It is built using the Django framework and Django REST framework. The API allows you to interact with a "person" resource, with dynamic parameter handling and data validation.</p>

<h2 id="prerequisites">Prerequisites</h2>
<p>Before you get started, make sure you have the following installed:</p>
<ul>
    <li>Python 3.x</li>
    <li>Django</li>
    <li>Django REST framework</li>
</ul>

<h2 id="setup">Setup</h2>
<ol>
    <li><strong>Clone this repository:</strong></li>
    <pre><code>git clone https://github.com/breezeconcept/HNGx_Task2.git</code></pre>
    <li><strong>Create a virtual environment (optional but recommended):</strong></li>
    <pre><code>python -m venv venv</code></pre>
    <li><strong>Activate the virtual environment (if created):</strong></li>
    <pre><code>source venv/bin/activate  # On Windows, use: venv\Scripts\activate</code></pre>
    <li><strong>Install project dependencies:</strong></li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li><strong>Apply database migrations:</strong></li>
    <pre><code>python manage.py migrate</code></pre>
    <li><strong>Start the development server:</strong></li>
    <pre><code>python manage.py runserver</code></pre>
</ol>
<p>The API will be accessible at <a href="http://localhost:8000/api/">http://localhost:8000/api/</a>.</p>

<h2 id="usage">Usage</h2>

<h3>API Endpoints</h3>

<h4>Create a Person:</h4>
<p><strong>Endpoint:</strong> /api/</p>
<p><strong>Method:</strong> POST</p>
<p><strong>Request Body Format:</strong></p>
<pre><code>json
{
  "name": "John Doe",
  "age": 30
}
</code></pre>

<h4>Fetch Details of a Person:</h4>
<p><strong>Endpoint:</strong> /api/&lt;int:pk&gt;/</p>
<p><strong>Method:</strong> GET</p>

<h4>Modify Details of an Existing Person:</h4>
<p><strong>Endpoint:</strong> /api/&lt;int:pk&gt;/</p>
<p><strong>Method:</strong> PUT</p>
<p><strong>Request Body Format:</strong></p>
<pre><code>json
{
  "name": "Updated Name",
  "age": 35
}
</code></pre>

<h4>Remove a Person:</h4>
<p><strong>Endpoint:</strong> /api/&lt;int:pk&gt;/</p>
<p><strong>Method:</strong> DELETE</p>

<h3>Sample Requests and Responses</h3>

<h4>Create a Person (POST):</h4>
<p><strong>Request:</strong></p>
<pre><code>http
POST /api/
Content-Type: application/json

{
  "name": "John Doe",
  "age": 30
}
</code></pre>
<p><strong>Response (201 Created):</strong></p>
<pre><code>json
{
  "id": 1,
  "name": "John Doe",
  "age": 30
}
</code></pre>

<h4>Fetch Details of a Person (GET):</h4>
<p><strong>Request:</strong></p>
<pre><code>http
GET /api/1/
</code></pre>
<p><strong>Response (200 OK):</strong></p>
<pre><code>json
{
  "id": 1,
  "name": "John Doe",
  "age": 30
}
</code></pre>

<h4>Modify Details of an Existing Person (PUT):</h4>
<p><strong>Request:</strong></p>
<pre><code>http
PUT /api/1/
Content-Type: application/json

{
  "name": "Updated Name",
  "age": 35
}
</code></pre>
<p><strong>Response (200 OK):</strong></p>
<pre><code>json
{
  "id": 1,
  "name": "Updated Name",
  "age": 35
}
</code></pre>

<h4>Remove a Person (DELETE):</h4>
<p><strong>Request:</strong></p>
<pre><code>http
DELETE /api/1/
</code></pre>
<p><strong>Response (204 No Content)</strong></p>

<h2 id="known-limitations-and-assumptions">Known Limitations and Assumptions</h2>
<ul>
    <li>The API assumes that names are alphanumeric and can contain spaces.</li>
    <li>Validation for age is not included in this example but can be added based on specific requirements.</li>
    <li>Error handling for exceptional cases is minimal in this example and should be extended for production use.</li>
</ul>

<h2 id="deployment">Deployment</h2>
<p>To deploy this API in a production environment, follow these steps:</p>
<ol>
    <li>Set up a production-ready database (e.g., PostgreSQL, MySQL).</li>
    <li>Configure production settings in settings.py (e.g., security settings, database settings).</li>
    <li>Deploy the API using a web server or hosting platform of your choice (e.g., Gunicorn, Apache, Heroku).</li>
    <li>Configure environment variables for sensitive information (e.g., API keys, database credentials).</li>
    <li>Set up domain and SSL certificates for secure communication.</li>
    <li>Monitor and maintain your production server regularly.</li>
</ol>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Please fork this repository, create a branch, and submit a pull request with your changes.</p>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>

</body>
</html>
