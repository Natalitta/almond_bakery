# Almond Bakery
Almond Bakery is a fictional bakery, which provides service of baking and delivering cakes. The app is a designed provide customers with a simple, easy to use system where they can view different cakes, order them and edit or delete their reservations. In addition, it allows the administrator to manage the menu and bookings through admin panel. 


<img src="media/mockup.png" alt="app mockapp">

To see the live app please follow this <a href="https://almond-bakery-f92f9dfc55d0.herokuapp.com/" target="_blank"> link to the web app</a>

## User-Experience-Design

### The-Strategy-Plane

Site Goals
1)	For admin: Manage the menu displayed on the website, keep track of upcoming orders, edit, mark complete and delete if necessary.
2)	For customers: Make reservations in a simple way without the need to call or come to the bakery, to update or cancel their orders.

### Agile Planning
This project was developed using agile methodology by delivering small features in incremental sprints.
The user stories were assigned to epics, prioritized under the labels: Must have, should have, could have. 
"Must have" stories were completed first to ensure that core features were completed first to make the project ready to use. 

There was created a Kanban board using GitHub projects. 
It can be found here: <a href="https://github.com/users/Natalitta/projects/7" target="_blank">link to the project</a>

#### Epics (Milestones):
There are 4 Epics (Milestones):

<img src="media/milestones.png" alt="project milestones">

* Menu:
    * As a user, I'd like to view the menu so that I can make up my mind.
    * As an owner, I'd like to be able to edit the menu so that it is always up to date.
    * As an owner, I'd like to have a nice menu on the home page with beautiful pictures so that customers want to order my cakes.
    * As an owner, I'd like to be able to add menu items so that I can offer new options to my customers when available.
    * As an owner, I'd like to be able to delete menu items so that the menu is always up to date.

* Bookings:
    * As a user, I'd like to be able to place my order easily through the site so that I can order a cake quickly and easily.
    * As a user, I'd like to be able to view my orders so that I can check them.
    * As a user, I'd like to be able to delete my order so that I can save my time and not phone to cancel my booking.
    * As a user, I'd like to be able to edit my booking so that I can keep it relevant.
    * As an owner, I'd like to be able to mark the orders if I have already sent them so that I can track my delivery process.    
    * As an owner, I'd like to see all the information required from a customer so that I can deliver the right order.

* Basic Setup:
    * As an owner, I'd like to have the same navigation and footer for all my site pages so that users feel more comfortable.
    * As an owner, I'd like to have a home page with a menu and navigation, a button to place an order so that site is convenient to use and gives an opportunity to order straight away.
    * As an owner, I'd like to have access to menu items and bookings, all data so that I can view and manage them.
    * As an owner, I'd like to have links to my social media accounts so that I have more connections with my audience.

* Deployment:
    * As an owner, I'd like to have my site up and running so that customers can utilise it.
    * As an owner, I'd like the app to be tested so that I can be sure that everything works properly.
    * As a developer, I must write a README file and fill it with all details so that it gives all information about the website.

### The-Scope-Plane

•	Home page with bakery menu 
•	Drop-down navigation menu for mobile devices
•	Ability to perform CRUD functionality on Bookings 
•	Responsive Design - Site should be fully functional on all devices from 320px up

### The-Structure-Plane
Features
USER STORY - As an owner, I'd like to have a home page with a menu and navigation, a button to place an order so that site is convenient to use and gives an opportunity to order straight away.
Implementation:
1)	Navigation Menu
The Navigation contains links for Home, Order Cake, My Orders and has allauth options.
The following navigation items are available on all pages:
•	Home -> index.html - Visible to all
•	Login -> login.html - Visible to logged out users
•	Register -> signup.html - Visible to logged out users
•	Logout -> logout.html - Visible to logged in users 
•	Order Cake -> booking.html - Visible to all 
•	My orders -> all_bookings.html – Visible to logged in users
The navigation menu is the same for all pages and displayed fully on big screens and drops down as a hamburger menu on smaller devices. It makes web application comfortably viewable on any device without taking up too much space on mobile devices.

2)	Home Page
The home page contains the menu of the bakery. This makes it clear from the first glance, what the purpose of the website is.
Under the cards with cakes there is a button 'Order your favourite cake'. This button allows the user to order a cake quickly without browsing the website.
USER STORY - As an owner, I'd like to have links to my social media accounts so that I have more connections with my audience.
Implementation:
Footer

A footer at the bottom of the site contains social media links: Twitter, Facebook and Instagram. The links open in new tabs because they lead users away from the site. Users can follow the bakery on social media to see special offers. 


## Testing
### Validator Testing
The application was tested to ensure that the code passes the official validators.
#### HTML

#### CSS
#### JavaScript
#### Python
#### Accessibility Testing

To test Accessibility the Wave tool was used.

Testing was focused to ensure the following criteria were met:

    All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
    Color contrasts meet a minimum ratio as specified in WCAG 2.1 Contrast Guidelines
    Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
    All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
    All not textual content had alternative text or titles so descriptions are read out to screen readers
    HTML page lang attribute has been set
    Aria properties have been implemented correctly
    WCAG 2.1 Coding best practices being followed

#### Lighthouse Testing
#### Functional Testing