Supabase from PipeDream
=======================

First, create a supabase account. I use my
GitHub account to log in.

In supabase:

1. Go to `https://supabase.com/dashboard/projects`
2. click on 'New Project'
3. Choose whatever org you want
4. Name the project (I used 'ToDo')
5. Click on "Generate a Password"
6. Click on the "copy" icon
7. Save the password somewhere
	UEl9TMR2JVAZBJ9F
8. Click on "Create new project"
9. Click on the database icon on the left
10. Click on the gear icon on the left (`Project Settings`)
11. Click on `database` in the almost leftmost menu
	- this will display the information needed next

Second, create an account at pipedream.com

In pipedream:

1. Click on `Accounts` in the left menu
2. Click on 'CONNECT AN APP'
3. Search for "postgres"
4. Click on "PostgreSQL"
5. Fill in the form:
	- into `Password`, paste in the previously copied password
	- into 'host' copy string in supabase 'Host' field
	- into 'port' copy string in supabase 'Port' field
	- into 'user' copy string in supabase 'User' field
	- into 'database' copy string in supabase 'Database Name' field
	- enter a nickname if you wish (I used "TestDB")
	- click the 'Save' button

You now have a supabase database you can use from PipeDream

Create a workflow to initialize our database
--------------------------------------------

In pipedream:

1. Click on `Workflows`
2. Click on `New`
3. Click on `HTTP / Webhook`
4. Click on `HTTP Requests with a body`
5. Click 'Save and Continue"
6. Copy the provided URL and save it somewhere
	https://eokz59uelix41u2.m.pipedream.net
7. Click on "Generate Test Event"
8. Enter this in 'Raw Request Body':


```sql
{
	"op": "create table",
	"sql": "create table if not exists ToDos (Name varchar(64), Done: boolean, Type varchar(16));"
}
```

10. Click on 'Send HTTP Request'
11. Click on 'Continue'
12. Select the step 'PostgreSQL' as the next step
13. Select 'Execute Custom Query'
14. In field `SQL Query`, enter `{{steps.trigger.event.sql}}`
15. Click on 'Test'
	- you should get a successful result and if you check
		supabase, the table should be created.

`https://eopteve249k9dl9.m.pipedream.net`

Use cURL to send an HTTP request:

```text
curl -d '{
  "message": "Wow!!! Pipedream IS awesome and easy to use!!!"
}'   -H "Content-Type: application/json"   YOUR-TRIGGER-URL-GOES-HERE
```

