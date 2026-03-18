# Pens Nexus

## Summary
The purpose of this project is to create a site that can be used by people to share their stories and novels with readers and community members in a flexible way.

The goal is to allow members to write, organize, and share their work with as little censorship as possible, while allowing for various forms of monetization.

## Features
The following is a list of features that are intended to be in the final version of the site.

* The ability to create and edit stories and novels, being able to break them up into books, sections/acts, chapters, and scenes. Possibly even lines.
* The ability to share stories in a granular way, with collaborators or fans.
* The ability to leave/accept feedback on stories.
* An internal messaging system.
* An internal currency for use in supporting authors, running subscriptions, and other related tasks.
* The ability to group books/stories into collections such as series or libraries.
* The ability to have an "imprint" representing a group of people.
* An issue tracking system to help track development and problems with the site.
* Ability to export books to various formats (Pandoc may be helpful here.)
* More to come.

## Road Map

### The Issue Tracker
This will be the first element I will create. At its core it will be the simplest element, but will also require all of the same basic parts as the rest of the system. It will require me to get the database functionality up and going as well as authentication. It will also require me to pair the frontend and the backend.

### User Profiles and Aliases
The ability to create aliases within the system and use them to interact with groups.

### The Messaging System
Next, I will get the internal messaging up and going. In its most basic form, if will be an internal mail system. Instant messaging is possible at a later date as well.

### User Posts and Feeds
At this stage we will develop the ability for authors (users in general really) to make posts similar to a blog feed. Once the initial functionality is in place, we will add the document editor that will become the foundation of the rest of the site.

### Imprints
The ability to create user groups, and share communications across the group. This can also be thought of as the "Publisher" of books and stories that are attributed to the Imprint.

### Stories
This is where we will actually start to build in the support needed to start creating books. At first we will focus on single chapters that work well for short stories or serials (such as fanfics and the like).

### Collections and Libraries
We will allow users or imprints to gather collections of stories/books into organized lists. These collections will be owned/organized by a user profile or an imprint.

### Books
This is where we will start working on features needed for more complex stories and books. We will allow them to be organized into

#### Chapters
The basic organizational element of most books.

#### Sections
Sections, Parts, or a Acts are a higher level organizational structure.

#### Scenes
Chapters can be organized into Scenes.

### Author Pages
The ability to create an Author page for a user’s aliases.

## Features

### Authentication

#### Basics
When the user logs in, the API will generate a token that ties the user’s session to their account. The token will be cached in the database to facilitate long term access, but will be cleared when the user logs out of the session, or requests to clear all tokens.

If a token is requested by the client, but doesn’t exist in the database, the session will be logged out and redirected to the login page.


## Milestones: Roadmap in Depth

### Milestone X: Basic Requirements
These items will be implemented as appropriate, starting from the beginning and updated as needed. They can be thought of somewhat as Milestone 0 as well.

### Milestone 1: User Authentication
- [ ] Create User data classes and tables.
- [ ] Add code to insert and retrieve users from the database.
- [ ] Create setup script to create initial admin user.
- [ ] Add code/forms to register a user.
- [ ] Add code to verify a user.
- [ ] Add code to open/close registration for new users. (Implies Admin Dashboard)
- [ ] Add code to authenticate and create tokens.
- [ ] Add code to verify that user is authenticated.
- [ ] Add code to log out.
- [ ] Make header offer a login button if not authenticated.
- [ ] Add code to create default profile when registering.
- [ ] Unit Testing.

### Milestone 2: Issue Tracker
- [ ] Implement the Main Menu
- [ ] Add tracker to menu
- [ ] Create a stub for the landing page.
    * Anonymous users can see tracker.
    * Must be logged in to create issues or comment.
- [ ] Create Issue classes and tables.
- [ ] Add code to create an issue ticket.
- [ ] Create tables and classes for Comments.
    * Comment will be a class used across various pages.
    * It should be implemented to decide the associated table based on type.
    * Perhaps get comments where type == issue and target_id == this.id
- [ ] Implement code to add issues.
- [ ] Implement code to add comments.
- [ ] Implement the rest of the CRUD.
- [ ] Unit testing.

### Milestone 3: Initial Live Server Setup
- [ ] Configure Dev server
- [ ] Upload and build files
- [ ] Create Admin user and profile
- [ ] Start server for testing.
- [ ] Register  normal User.
- [ ] Create and comment on a few issues in the issue tracker.
- [ ] Get friends to play around with the issue tracker.

### Milestone 4: Ability to vote on Feature Requests
* Votes are anonymous
* Votes tied to User not Profile
* Options will be Yes or No. Anything other than that should go into the comments.



## Current Known Challenges

### Internal Currency/Tokens
In addition to the implementation element, which I can start work on early, the internal currency will not be able to function as an actual value store until I am able to determine all of the necessary regulatory elements. I will go into more detail on this when I have time to dig into the details. In early stages, these tokens will function more like “Karma” points do on other sites.
