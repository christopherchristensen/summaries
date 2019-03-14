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
* Authorization Server



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



## Authorization Server

* Trusted by protected resource
* Issues special purpose security credentials (OAuth Access Tokens) to clients
* Basic steps
  1. Client sends resource owner to auth server to request authorization of client
  2. Resource owner authenticates to the auth server with option to authorize or deny authorization of client
  3. Client is able to ask for subset of functionality or scopes
  4. If granted client can request access token from auth server
  5. Token can be used at protected resource to access API as granted by resource owner
* Resource owner's credentials never exposed to client
* Resource owner authenticates to auth server separately from anything used to communicate with client
* *"The authorization server gives us a mechanism to bridge the gap between client and protected resource."*

![auth-server-at-a-higher-level](/Users/christopher/Development/studies/github/summaries-me/infkol/mds/thesis/imgs/auth-server-at-a-higher-level.png)





## Without OAuth 2.0

* No authorization server

* Credential sharing
  * Requires user to have same credentials at client app and protected resource
  * Limits effectiveness of credential-theft technique to single security domain
  * e.g. Works if services and resources offered by same company
  * Copy resource owner's credentials and replay them to protected resource
  * Exposes user's password to client app
  * Client is impersonating user
  * *"Protected resource has no way of telling the difference between impersonating client and user."*
* Ask the user
  * If two services occupied by different security domains
  * Service ask user for username and password
  * Replay first then takes place
  * Credentials for client log in and protected resource don't need to match
  * Extremely dangerous (but common) practice
  * Still not applicable to all use cases 
    (e.g. nearly all federated, many multifactor, most higher-security login systems)
  * *"Ask for resource owner's credentials and replay them to protected resource."*
  * LDAPs work like this (similar to a "good" MIM-attack)
* universal / developer key
  * key issued to client
  * can call protected resources directly
  * only a good idea between two trusted parties
  * no credential sharing though
  * if credentials stolen, then resources completely exposed
  * *"A universal key that's good for opening the door no matter who locked it."*
* special password
  * password only used for sharing with third-party services
  * password not used for log in
  * pasted into app that they want to work for them
  * (closer to a desirable system)
  * user needn't to share credentials
  * resource needn't implicitly trust client to act properly on behalf of all users at all time
  * user required to generate, distribute and manage these special credentials in addition to primary passwords
  * since user manages credentials no correlation between client program an credentials
  * *"A special password (or token) that can be used to access just this protected resource."*



## Problems without OAuth 2.0

> expecially credentials sharing and ask the user

* possibly exposes user's primary credentials to potentially untrustworthy apps
* client has to store user's credentials in replayable fashion (often plaintext)
* client app is impersonating resource owner
  * no way of distinguishing whos who
  * rogue printer service can access other resources too (despite promises not to)
  * only way to prevent is by changing password
  * if you reuse same password somewhere else, printer might have access now to that too



## Delegating Access in OAuth 2.0

* end user delegates som part of their authority to access protected resource to the client app to act on their behalf
* To do that OAuth introduces new component: authorization server

