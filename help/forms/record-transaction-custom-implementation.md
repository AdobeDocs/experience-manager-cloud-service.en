---
title: Record a transaction for custom implementations
description: Use the TransactionRecorder API to record actions which are not accounted as transactions automatically
feature: Adaptive Forms, Foundation Components
exl-id: cb584f78-30af-4a58-be99-843352e8249c
role: "Admin, Developer, User"
---
# Record a transaction for custom implementations {#record-a-transaction-for-custom-implementations}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/forms/transaction-reports/transaction-reports-osgi/record-transaction-custom-implementation)                  |
| AEM as a Cloud Service     | This article         |

Use the TransactionRecorder API to record actions which are not accounted as transactions automatically.

You can use custom code to submit a PDF Form. Or, you submit a form using custom methods instead of using submit methods provided with AEM Forms. All the previously mentioned actions and custom implementations of AEM Forms APIs are not accounted as transactions. AEM Forms provide an API, [TransactionRecorder](https://javadoc.io/doc/com.adobe.aem/aem-forms-sdk-api/latest/com/adobe/aem/transaction/core/ITransactionRecorder.html), to record such actions as transactions.

To record a transaction, write the [standard sling servlet](https://experienceleague.adobe.com/docs/experience-manager-learn/forms/store-and-retrieve-af-with-2fa/create-servlet.html?lang=en) and call the servlet from a client to record a transaction. You can call the servlet using AJAX or any other standard method.

## Sample server-sided code {#sample-server-sided-code}

You can use the below sample code to run the TransactionRecorder API from a Java&trade; class using a custom OSGi bundle.

```java
import com.adobe.aem.transaction.core.ITransactionRecorder;
import com.adobe.aem.transaction.core.model.TransactionRecord;
import com.adobe.aem.transaction.core.exception.TransactionException;
import com.adobe.aem.transaction.core.FormsTransactionConstants;

@Reference
private ITransactionRecorder transactionRecorder;

doPost (SlingHttpServletRequest request, SlingHttpServletResponse response) {
    transactionRecorder.startContext();
    TransactionRecord txRecord = extractTxRecordFromRequest(request); //extract transaction relevant data from request
    try {
        bool success = doBillableWork();
        if (success) {
            transactionRecorder.recordTransaction(txRecord);
        }
    } catch (Exception e) {
        //exception handling
    } finally {
        transactionRecorder.endContext();
    }
}

//Here, it is assumed that txInfo is passed in Stringified json form in the ajax call (in data parameter). You can pass txInfo from client in any way that you find suitable.
private TransactionRecord extractTxRecordFromRequest(SlingHttpServletRequest request) {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(request.getInputStream()));
    Map<String, Object> txDataMap = new HashMap<String, Object>();
    String txData = bufferedReader.readLine();
    JSONObject txInfo= new JSONObject(txData );
    try {
        String resourceType= txInfo.getString("resourceType");
        String transactionType = txInfo.getString("transactionType");
        Integer transactionCount = (Integer)txInfo.get("transactionCount");
        //Extract all the relevant tx record attributes similarly and pass them in Transaction Record constructor as per the java doc}
        return new TransactionRecord(transactionCount, transactionType, resourceType, ..);
    } catch (JSONException e) {
        //exception handling
    } finally {
        bufferedReader.close();
    }
}

```

## Sample client-side code {#sample-client-side-code}

You can use the below sample code to call the servlet that has the `TransactionRecorder`API.

```javascript
$.ajax({
   type: 'POST',
   url: url, //servlet url
   contentType: 'application/json; UTF-8',
   data: JSON.stringify({transactionCount : 1,
                        transactionType: "SUBMIT",
                        resourceType: "FORM",
                        resourceSubType: "ADAPTIVE-FORM"}),
   success: successHandler,
   error: faultHandler
})

```

## Related Articles {#related-articles}

* [Transaction Reports Billable APIs](/help/forms/transaction-reports-billable-apis.md)
