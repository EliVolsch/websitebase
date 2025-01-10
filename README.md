# websitebase
websitebase


## Roadmap for developement

### Base
Make use fo the following technologies for the base:
* Django 
* Jinja

### Scope
We want to create a website with the following parameters listed below as an example. We want to create a website for an HOA company to be able to do some core features they require:

#### Communication
- Want to be able to notify people about inportant happenings - (A blog would be sufficient without the ability to comment)
- Handle complaints/queries - People should be able to get in touch with the trustees via email from the pages this should include the following:
  1) Applications - Pets, trailer storage, move-in, move-out, intercom changes, remotes, maintenance requests.
  2) complaints - If people want to complain they can do so anonnymously
  3) Queries - Levy statements and queries

#### Databases
We want to keep a database with the following information to be able to effectivley manage the complex:
- Residents - This includes tenants (People living here), and owners. We need information like: Email, telephone numbers, unit numbers vehicle registrations, makes, and models (if applicable) 
- Pets - We want to keep record of pets on the property and approval statu's therof should work together with the pet applications. This needs to have the following information: Pet name, type, breed, vetarany information, picture, and approval status
- Blogs - Keep track of any blogs that were posted and when the following info will be applicable. All effective info should be recorded
- Communications - A db keeping track of the communication requests submitted.

#### Pages
##### Django Admin page
The basic django admin page

##### Admin page
THe admin page should be separate from the django admin page and is a restricted page for only trustees. this should include the following pages:
- Resident info pages
- Blogs creation and publish page
- Commuications received page

##### Blogs page
The blogs page should have have all the blogs for people to read but can have blogs restriced to users.

##### Complains page
Restricted page for logged in users only

##### Normal information pages
THe rest of the normal pages like: Home, about, create profile, login

### Functonalities
- We should be able to receive and send information from the platform via email in the case of queries, complaint, blogs
- Add remove content in the case of blogs , pets, tenants and so on
   