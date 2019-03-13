# The Basics of OAuth 2.0?



## Topics

* What is OAuth 2.0
* What do developers do without OAuth
* How OAuth works
* What is OAuth 2.0 not



## What is OAuth 2.0?

* Delegation / security protocol
* A means of letting someone who controls a resource allow a software application to access that resource on their behalf without impersonating them
* Basic (naive) steps:
  1. app requests authorization from owner of resource
  2. app receives tokens to access resource



## Token

* Token explicitly represents a delegated right of access
  * Not necessarily all rights
  * Limited access to delegated actions by resource owner



## What does OAuth do?

* It is all about obtaining right of access from one component of a system to another
  * e.g. a client app wants access to a protected resource on behalf of a resource owner (usually end user)
* OAuth 2.0 framework enables third-party apps to obtain limited access to an HTTP service on behalf of a resource owner 
  * By orchestrating an approval interaction between resource owner and HTTP service, or
  * By allowing third-party app to obtain access on its own behalf



## Main Components of OAuth 2.0

* Resource Owner
* Protected Resource
* Client



## Resource Owner

* Has access to an API
* Can delegate access to that API
* Usually a person
* Person is generally assumed to have access to a web browser



## Protected Resource

* Component that resource owner has access to
* Many different Form, but mainly a web API
* APIs *can* often allow CRUD operations (not just download)



## Client

* Piece of software that accesses protected resource on behalf of resource owner
* Software that consumes the API that makes up the protected resource



## Without OAuth 2.0

* Credential sharing
  * Requires user to have same credentials at client app and protected resource
  * Limits effectiveness of credential-theft technique to single security domain
  * e.g. Works if services and resources offered by same company
  * Copy resource owner's credentials and replay them to protected resource
  * Exposes user's password to client app
  * Client is impersonating user
  * *Protected resource has no way of telling the difference between impersonating client and user.*
* Ask the user
  * If two services occupied by different security domains
  * Service ask user for username and password
  * Replay first then takes place
  * Credentials for client log in and protected resource don't need to match
  * Extremely dangerous (but common) practice
  * Still not applicable to all use cases
  * *Ask for resource owner's credentials and replay them to protected resource.*

