# Examples

> Collection of examples mentioned in class



## PDF Rendering

* Adding PDF rendering 
* How does this modify the attack surface?

```java
@Log
public class AccountServiceSQLImpl implements AccountService {
    
	...
        
	@RequestMapping(
        path = "/account/{accountId}", 
        produces = "application/pdf"
    ) 
        
    @SneakyThrows
	public @ResponseBody byte[] getAccountDetailsPdf( 	
        @PathVariable("accountId") String accountId) 
    {
        
		JasperPrint print = JasperFillManager
            .fillReport(
            	this.getClass()
            	.getClassLoader()
            	.getResourceAsStream("account_details.jasper"),
            	new HashMap(),
            	new JRBeanCollectionDataSource(Arrays.asList(
                    delegate.getAccountDetails(accountId)
                ))
        	); 
        
        //converting DOM representation into byte array
		return JasperExportManager.exportReportToPdf(print);
        
    }
    
}
```

* While rendering PDF it could write into a temporary file? (TODO)



