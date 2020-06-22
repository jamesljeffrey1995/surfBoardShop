# Surfboard Shop

<h2> The brief </h2>
<p1>To create a CRUD application using the technologies and methodologies that were taught to us during training.</p1>
<br>
<h3>My application</h3>
<p1>My project is a surfshop. The web application allows for the user to add items, modify the quantity, delete selected products and also buy other products</p1>
<br>
<h2>Architecture</h2>
<h3>Entity Relationship Diagrams</h3>
<h4>Initial plan</h4>

![new_erd](https://i.imgur.com/jKn9mtf.png)

<p1> The initial ERD was to meet the requirments of the project brief. It consists of a many to many relationship between the stock and the order. A user is able to make multiple orders with different products.</p1>

<h4>Updated Model</h4>
  
  ![erd](https://i.imgur.com/M808vOi.png)
  
<p1>The updated model has an orderline which allows for the many to many relationship. This takes the product ID and order ID which is assigned to the user, and allows for a calculation of the total. </p1>

<h4>Deployed Model</h4>

  ![erd_update](https://i.imgur.com/ZAerkSj.png)

<p1>The deployed model is the same as the updated model, but the user has a relationship to the stock, therefore when a product is made by the user, the user is assigned to it</p1>

![CI](https://i.imgur.com/XFJBrdJ.png)

<h2>Risk assessment</h2>

![risk assessment](https://i.imgur.com/YWCctuD.png)

<h2>User Stories</h2>

<p1>To track the progress of the project and layout what was needed, Trello was used to do this.</p1>

![User Stories](https://i.imgur.com/xOR6AyI.png)

<p1>The board has several collumns, this allowed to keep tabs on the progress. The application of MoSCoW method allowed for easier project tracking</p1>
<ul>
  <li><i>Product Backlog</i>: This showed the user stories that still needed to be completed</li>
  <li><i>Sprint</i>: This showed what had to be completed to the timebox, which was 24 hours, with 4 sprints</li>
  <li><i>In progress</i>: This shows what is currently being worked on</li>
  <li><i>Completed</i>: This shows all the user stories that have been completed </li>
</ul>

<h2>Testing</h2>

<h3>Unit Testing</h3>

<p1>Using pytest to create a coverage test of the application, 15 tests were made allowing for a 75% coverage. I then set jenkins pipeline up so that when anything is push to git, it is tested and the index.html is stored in a tests folder. That then triggers another job, which deploys the application.</p1>

![Coverage Report console](https://i.imgur.com/pSLRsV6.png)
![Coverage Report jenkins](https://i.imgur.com/pMjN7du.png)

<h2>Surfboard Forum Shop</h2>
<h3>Front End Design</h3>
<p1>The design is made using HTML</p1><br>
<p1>When the user navigates via the url, they are directed to the homepage</p1><br>
<p1>Using the navigate bar, they are able to register an account. These details are stored in the Users table</p1>

![app](https://i.imgur.com/6kPfQzX.png)

<p1>The user is then redirected to the login page, where they can input their credentials</p1>

![app1](https://i.imgur.com/zuyNo0E.png)

<p1>The user is then redirected to the homepage, where a new navigation bar is presented</p1>

![app2](https://i.imgur.com/5jFqD3n.png)

<p1>The post page allows for the user to post a surfboard they wish to sell.</p1>

![app3](https://i.imgur.com/Mj7ybjN.png)

<p1>The user is then redirected back to the homepage, where their item is then presented</p1>

![app4](https://i.imgur.com/rpAaU13.png)

<p1>The user can click on the item, and they are directed to the products page of that item. They can then input an amout they want to buy</p1>

![app5](https://i.imgur.com/2FeUjLY.png)

<p1>They are then redirected back to the homepage, and is shown that the quantity of the item has reduced. If the user input a quantity that is over the amount of stock, then they are redirected to the homepage and the order doesnt go through</p1>

![app6](https://i.imgur.com/5xNn01V.png)

<p1>If the user then navigates to 'your shop', then they can view the items they uploaded</p1>

![app7](https://i.imgur.com/g2PWGBD.png)


<p1>If the user clicks on the item name, they are directed to update page, where they can change the quantity of the product, they are then redirected back to the homepage</p1>

![app8](https://i.imgur.com/MlrfC7n.png)
![app9](https://i.imgur.com/n8zVbxH.png)


<p1>The user can also delete an item in the user shop, once they press delete, they are redirected to the home page</p1>

![app10](https://i.imgur.com/ZUlED00.png)
![app11](https://i.imgur.com/wQ7m4r2.png)

<p1>If the user is not logged in, then the Href is removed from the products and the user cannot navigate to the buy page</p1>

<h2>Known Issues</h2>
<ul>
  <li>Dynamic url for products, if the product is deleted, the user can still go to the page but displays nothing apart from the layout.html</li>
  <li>Gunicorn is deployed constantly</li>
  <li>Email says it succesfully sent email, but no email is recieved</li> 
</ul>

<h2>Future improvements</h2>
<ul>
  <li>Allow for the user to filter styles of boards, length and price</li>
  <li>Allow for the user to see their orders</li>
  <li>Group the orders that were made in the same session and create a checkout for all items</li>
  <li>Improve the front end, and make it more visually appealing</li>
</ul>

<h2>Authors</h2>
<p1>James Jeffrey</p1>
