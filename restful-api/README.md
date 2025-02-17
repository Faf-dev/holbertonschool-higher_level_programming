# Intro to RESTful API

## 1 - Difference between HTTP and HTTPS

### **HTTP** 

Stands for Hypertext transfer protocol. It's used for transferring data over a network. Most information that is sent over the internet, including website content and API calls, uses the HTTP protocol. There are two main kinds of HTTP messages : requests and responses

### **HTTPS**

The S stands for "secure". HTTPS uses TLS (or SSL) to encrypt HTTP requests and responses. Instead of the text, an attacker would see a bunch of seemingly random characters.

### Exemple :

#### Instead of :  

GET /hello.txt HTTP/1.1  
User-Agent: curl/7.63.0 libcurl/7.63.0 OpenSSL/1.1.l zlib/1.2.11  
Host: www.example.com  
Accept-Language: en

#### The attacker will see something like this :  

t8Fw6T8UV81pQfyhDkhebbz7+oiwldr1j2gHBB3L3RFTRsQCpaSnSBZ78Vme+DpDVJPvZdZUZHpzbbcqmSW1+3xXGsERHg9YDmpYk0VVDiRvw1H5miNieJeJ/FNUjgH0BmVRWII6+T4MnDwmCMZUI/orxP3HGwYCSIvyzS3MpmmSe4iaWKCOHQ==

## 2 - Depiction of the structure of an HTTP request and response

### **HTTP request**

**An HTTP request looks like this** :

GET /hello.txt HTTP/1.1  
User-Agent : curl/7.63.0 libcurl/7.63.0 OpenSSL/1.1.l zlib/1.2.11  
Host : www.example.com  
Accept-Language : en  

**An HTTP response looks like this** :

HTTP/1.1 200 OK  
Date : Wed, 30 Jan 2019 12:14:39 GMT  
Server : Apache  
Last-Modified : Mon, 28 Jan 2019 11:17:01 GMT  
Accept-Ranges : bytes  
Content-Length : 12  
Vary : Accept-Encoding  
Content-Type : text/plain  

Hello World !  

## 3 - Lists of common HTTP methods

### Request method :

- **OPTIONS :**  
    - **Description**: Describes the communication options for the target resources.
    - **Use Case**: Discovering allowed methods and other options for a resource.

- **GET :**  
    - **Description**: Retrieves data from a server.
    - **Use Case**: Fetching a web page or data from an API.

- **HEAD :**
    - **Description**: Retrieves the headers of a resource without the body.
    - **Use Case**: Checking if a resource exists or getting metadata without downloading the entire resource.

- **POST :**  
    - **Description**: Sends data to the server to create a new resource.
    - **Use Case**: Submitting a form or uploading a file.

- **PUT :**  
    - **Description**: Updates an existing resource or creates a new resource if it does not exist
    - **Use Case**: Updating user information or replacing a resource.

- **DELETE :**  
    - **Description**: Removes a resource from the server.
    - **Use Case**: Deleting a user account or removing a file.
  
- **TRACE :**  
    - **Description**: Echoes back the received request, allowing the client to see what (if any) changes or additions have been made by intermediate servers.
    - **Use Case**: Used for diagnostic purposes to trace the path of a request.

- **CONNECT :**  
    - **Description**: Establishes a tunnel to the server identified by the target resource.
    - **Use Case**: Used for SSL (HTTPS) connections through an HTTP proxy.

- **PATCH :**
    - **Description**: Partially updates an existing resource.
    - **Use Case**: Modifying specific fields of a resource without sending the entire resource.

## 3.1 - Lists of HTTP status codes 

### **1xx : Informational**  
These indicate that the request has been received and is being processed.

- **100** Continue  
  - **Description**: The server has received the request headers and the client should proceed with the request body.  
  - **Scenario**: Used for large POST requests to ensure the server is ready.  

- **101** Switching Protocols  
  - **Description**: The server is switching protocols as requested.  
  - **Scenario**: Switching from HTTP to WebSocket.  


### **2xx : Success**  
These indicate that the request was successfully processed.

- **200** OK  
  - **Description**: The request was successful.  
  - **Scenario**: Successfully fetching a web page.  

- **201** Created  
  - **Description**: The request was successful, and a new resource was created.  
  - **Scenario**: A new user is successfully registered.  

- **204** No Content  
  - **Description**: The request was successful, but there is no content to return.  
  - **Scenario**: Deleting a resource where no response body is needed.  


### **3xx : Redirection**  
These indicate that further action is needed to complete the request.

- **301** Moved Permanently  
  - **Description**: The requested resource has been permanently moved to a new URL.  
  - **Scenario**: Redirecting an old URL to a new one.  

- **302** Found (Temporary Redirect)  
  - **Description**: The resource is temporarily available at a different URL.  
  - **Scenario**: Redirecting users while a website is under maintenance.  

- **304** Not Modified  
  - **Description**: The resource has not changed since the last request.  
  - **Scenario**: Used for caching purposes to prevent unnecessary data transfer.  


### **4xx : Client Errors**  
These status codes indicate that the client seems to have made an error.

- **400** Bad Request  
  - **Description**: The server could not understand the request due to invalid syntax.  
  - **Scenario**: Sending a malformed JSON request.  

- **401** Unauthorized  
  - **Description**: Authentication is required and has failed or not been provided.  
  - **Scenario**: Accessing a private API without a valid token.  

- **403** Forbidden  
  - **Description**: The client does not have permission to access the resource.  
  - **Scenario**: Trying to view a restricted page without the proper rights.  

- **404** Not Found  
  - **Description**: The requested resource does not exist.  
  - **Scenario**: Trying to access a page that does not exist.  

- **429** Too Many Requests  
  - **Description**: The client has sent too many requests in a short period.  
  - **Scenario**: Being rate-limited by an API due to excessive requests.  

### **5xx : Server Errors**  
These indicate that the server encountered an issue while processing the request.

- **500** Internal Server Error  
  - **Description**: A generic error message indicating an issue on the server.  
  - **Scenario**: A bug in server-side code causing a failure.  

- **502** Bad Gateway  
  - **Description**: The server received an invalid response from an upstream server.  
  - **Scenario**: A proxy server failing to get a valid response.  

- **503** Service Unavailable  
  - **Description**: The server is temporarily unavailable due to overload or maintenance.  
  - **Scenario**: A website is down for maintenance.  

- **504** Gateway Timeout  
  - **Description**: The server did not get a response from an upstream server in time.  
  - **Scenario**: A request taking too long due to network issues.  