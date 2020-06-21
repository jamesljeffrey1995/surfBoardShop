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

<p1>Using pytest to create a coverage test of the application, 15 tests were made allowing for a 75% coverage</p1>

![Coverage Report](https://i.imgur.com/rn76lG0.png)

<h2>Surfboard Forum Shop</h2>
<h3>Front End Design</h3>

![app](https://i.imgur.com/6kPfQzX.png)
![app1](https://i.imgur.com/zuyNo0E.png)
![app2](https://i.imgur.com/5jFqD3n.png)
![app3](https://i.imgur.com/Mj7ybjN.png)
![app4](https://i.imgur.com/rpAaU13.png)
![app5](https://i.imgur.com/2FeUjLY.png)
![app6](https://i.imgur.com/5xNn01V.png)
![app7](https://i.imgur.com/g2PWGBD.png)
![app8](https://i.imgur.com/MlrfC7n.png)
![app9](https://i.imgur.com/n8zVbxH.png)
![app10](https://i.imgur.com/ZUlED00.png)
![app11](https://i.imgur.com/wQ7m4r2.png)
![app12](https://i.imgur.com/pQjTlEy.png)
![app11](https://i.imgur.com/wGrXMas.png)
![app1](https://i.imgur.com/wIMs0Gq.png)
