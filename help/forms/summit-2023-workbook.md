---
title: Build Engaging Forms Using Core Components and Headless
seo-title: Build Engaging Forms Using Core Components and Headless
description: Build Engaging Forms Using Core Components and Headless
seo-description: Build Engaging Forms Using Core Components and Headless
topic-tags: develop
hide: yes
hidefromtoc: yes
exl-id: e1eb0812-c92e-4a18-aabb-5a70b9e6fc7d
---
# Build Engaging Forms Using Core Components and Headless

## Lab Overview

In this hands-on lab, you learn:

How to use AEM Forms to easily create adaptive forms using the latest core components which are consistent with AEM Sites, enable omnichannel data capture experiences by delivering the adaptive forms as headless forms to web, mobile, and chat. You also learn best practices around styling, customizations, and front-end development.

## Key takeaways

*   **Business Agility**: As a business user, I can author Form experience for multiple channels easily.

*   **Power to frontend developer**: As a frontend developer, I can control the end-user experience using headless forms.

*   **Developer Velocity**: As a developer, I can easily and consistently customize Sites and Forms components.

## Prerequisites


+++AEM Forms as Cloud Service sandbox



<table>
        <thead>
            <tr><th>Lab ID</th><th>Author instance URL</th><th>Publish Instance URL</th></tr>           
        </thead>
        <tbody>
            <tr><td>L716001</td><td>https://author-p105303-e986623.adobeaemcloud.com</td><td>https://publish-p105303-e986623.adobeaemcloud.com</td></tr><tr><td>L716002</td><td>https://author-p106405-e993047.adobeaemcloud.com</td><td>https://publish-p106405-e993047.adobeaemcloud.com</td></tr><tr><td>L716003</td><td>https://author-p106406-e993049.adobeaemcloud.com</td><td>https://publish-p106406-e993049.adobeaemcloud.com</td></tr><tr><td>L716004</td><td>https://author-p106398-e993114.adobeaemcloud.com</td><td>https://publish-p106398-e993114.adobeaemcloud.com</td></tr><tr><td>L716005</td><td>https://author-p106407-e993048.adobeaemcloud.com</td><td>https://publish-p106407-e993048.adobeaemcloud.com</td></tr><tr><td>L716006</td><td>https://author-p106408-e993155.adobeaemcloud.com</td><td>https://publish-p106408-e993155.adobeaemcloud.com</td></tr><tr><td>L716007</td><td>https://author-p106343-e993067.adobeaemcloud.com</td><td>https://publish-p106343-e993067.adobeaemcloud.com</td></tr><tr><td>L716008</td><td>https://author-p106399-e993108.adobeaemcloud.com</td><td>https://publish-p106399-e993108.adobeaemcloud.com</td></tr><tr><td>L716009</td><td>https://author-p106344-e993064.adobeaemcloud.com</td><td>https://publish-p106344-e993064.adobeaemcloud.com</td></tr><tr><td>L716010</td><td>https://author-p106409-e993051.adobeaemcloud.com</td><td>https://publish-p106409-e993051.adobeaemcloud.com</td></tr><tr><td>L716011</td><td>https://author-p106345-e993060.adobeaemcloud.com</td><td>https://publish-p106345-e993060.adobeaemcloud.com</td></tr><tr><td>L716012</td><td>https://author-p106346-e993061.adobeaemcloud.com</td><td>https://publish-p106346-e993061.adobeaemcloud.com</td></tr><tr><td>L716013</td><td>https://author-p106410-e993153.adobeaemcloud.com</td><td>https://publish-p106410-e993153.adobeaemcloud.com</td></tr><tr><td>L716014</td><td>https://author-p106502-e993073.adobeaemcloud.com</td><td>https://publish-p106502-e993073.adobeaemcloud.com</td></tr><tr><td>L716015</td><td>https://author-p106401-e993112.adobeaemcloud.com</td><td>https://publish-p106401-e993112.adobeaemcloud.com</td></tr><tr><td>L716016</td><td>https://author-p106452-e993115.adobeaemcloud.com</td><td>https://publish-p106452-e993115.adobeaemcloud.com</td></tr><tr><td>L716017</td><td>https://author-p106453-e993113.adobeaemcloud.com</td><td>https://publish-p106453-e993113.adobeaemcloud.com</td></tr><tr><td>L716018</td><td>https://author-p106411-e993050.adobeaemcloud.com</td><td>https://publish-p106411-e993050.adobeaemcloud.com</td></tr><tr><td>L716019</td><td>https://author-p106454-e993116.adobeaemcloud.com</td><td>https://publish-p106454-e993116.adobeaemcloud.com</td></tr><tr><td>L716020</td><td>https://author-p106347-e993063.adobeaemcloud.com</td><td>https://publish-p106347-e993063.adobeaemcloud.com</td></tr><tr><td>L716021</td><td>https://author-p106455-e993109.adobeaemcloud.com</td><td>https://publish-p106455-e993109.adobeaemcloud.com</td></tr><tr><td>L716022</td><td>https://author-p106456-e993110.adobeaemcloud.com</td><td>https://publish-p106456-e993110.adobeaemcloud.com</td></tr><tr><td>L716023</td><td>https://author-p106466-e993291.adobeaemcloud.com</td><td>https://publish-p106466-e993291.adobeaemcloud.com</td></tr><tr><td>L716024</td><td>https://author-p106413-e993156.adobeaemcloud.com</td><td>https://publish-p106413-e993156.adobeaemcloud.com</td></tr><tr><td>L716025</td><td>https://author-p106348-e993066.adobeaemcloud.com</td><td>https://publish-p106348-e993066.adobeaemcloud.com</td></tr><tr><td>L716026</td><td>https://author-p106414-e993154.adobeaemcloud.com</td><td>https://publish-p106414-e993154.adobeaemcloud.com</td></tr><tr><td>L716027</td><td>https://author-p106349-e993065.adobeaemcloud.com</td><td>https://publish-p106349-e993065.adobeaemcloud.com</td></tr><tr><td>L716028</td><td>https://author-p106415-e993152.adobeaemcloud.com</td><td>https://publish-p106415-e993152.adobeaemcloud.com</td></tr><tr><td>L716029</td><td>https://author-p106350-e993068.adobeaemcloud.com</td><td>https://publish-p106350-e993068.adobeaemcloud.com</td></tr><tr><td>L716030</td><td>https://author-p106351-e993062.adobeaemcloud.com</td><td>https://publish-p106351-e993062.adobeaemcloud.com</td></tr><tr><td>L716031</td><td>https://author-p106417-e993158.adobeaemcloud.com</td><td>https://publish-p106417-e993158.adobeaemcloud.com</td></tr><tr><td>L716032</td><td>https://author-p106418-e993159.adobeaemcloud.com</td><td>https://publish-p106418-e993159.adobeaemcloud.com</td></tr><tr><td>L716033</td><td>https://author-p106503-e993080.adobeaemcloud.com</td><td>https://publish-p106503-e993080.adobeaemcloud.com</td></tr><tr><td>L716034</td><td>https://author-p106457-e993125.adobeaemcloud.com</td><td>https://publish-p106457-e993125.adobeaemcloud.com</td></tr><tr><td>L716035</td><td>https://author-p106504-e993081.adobeaemcloud.com</td><td>https://publish-p106504-e993081.adobeaemcloud.com</td></tr><tr><td>L716036</td><td>https://author-p106458-e993120.adobeaemcloud.com</td><td>https://publish-p106458-e993120.adobeaemcloud.com</td></tr><tr><td>L716037</td><td>https://author-p106419-e993160.adobeaemcloud.com</td><td>https://publish-p106419-e993160.adobeaemcloud.com</td></tr><tr><td>L716038</td><td>https://author-p106420-e993162.adobeaemcloud.com</td><td>https://publish-p106420-e993162.adobeaemcloud.com</td></tr><tr><td>L716039</td><td>https://author-p106517-e993235.adobeaemcloud.com</td><td>https://publish-p106517-e993235.adobeaemcloud.com</td></tr><tr><td>L716040</td><td>https://author-p106506-e993079.adobeaemcloud.com</td><td>https://publish-p106506-e993079.adobeaemcloud.com</td></tr><tr><td>L716041</td><td>https://author-p106507-e993074.adobeaemcloud.com</td><td>https://publish-p106507-e993074.adobeaemcloud.com</td></tr><tr><td>L716042</td><td>https://author-p106508-e993075.adobeaemcloud.com</td><td>https://publish-p106508-e993075.adobeaemcloud.com</td></tr><tr><td>L716043</td><td>https://author-p106421-e993163.adobeaemcloud.com</td><td>https://publish-p106421-e993163.adobeaemcloud.com</td></tr><tr><td>L716044</td><td>https://author-p106459-e993121.adobeaemcloud.com</td><td>https://publish-p106459-e993121.adobeaemcloud.com</td></tr><tr><td>L716045</td><td>https://author-p106467-e993292.adobeaemcloud.com</td><td>https://publish-p106467-e993292.adobeaemcloud.com</td></tr><tr><td>L716046</td><td>https://author-p106518-e993234.adobeaemcloud.com</td><td>https://publish-p106518-e993234.adobeaemcloud.com</td></tr><tr><td>L716047</td><td>https://author-p106511-e993076.adobeaemcloud.com</td><td>https://publish-p106511-e993076.adobeaemcloud.com</td></tr><tr><td>L716048</td><td>https://author-p106512-e993077.adobeaemcloud.com</td><td>https://publish-p106512-e993077.adobeaemcloud.com</td></tr><tr><td>L716049</td><td>https://author-p106460-e993124.adobeaemcloud.com</td><td>https://publish-p106460-e993124.adobeaemcloud.com</td></tr><tr><td>L716050</td><td>https://author-p106519-e993237.adobeaemcloud.com</td><td>https://publish-p106519-e993237.adobeaemcloud.com</td></tr><tr><td>L716051</td><td>https://author-p106513-e993084.adobeaemcloud.com</td><td>https://publish-p106513-e993084.adobeaemcloud.com</td></tr><tr><td>L716052</td><td>https://author-p106461-e993122.adobeaemcloud.com</td><td>https://publish-p106461-e993122.adobeaemcloud.com</td></tr><tr><td>L716053</td><td>https://author-p106514-e993082.adobeaemcloud.com</td><td>https://publish-p106514-e993082.adobeaemcloud.com</td></tr><tr><td>L716054</td><td>https://author-p106462-e993123.adobeaemcloud.com</td><td>https://publish-p106462-e993123.adobeaemcloud.com</td></tr><tr><td>L716055</td><td>https://author-p106463-e993127.adobeaemcloud.com</td><td>https://publish-p106463-e993127.adobeaemcloud.com</td></tr><tr><td>L716056</td><td>https://author-p106515-e993083.adobeaemcloud.com</td><td>https://publish-p106515-e993083.adobeaemcloud.com</td></tr><tr><td>L716057</td><td>https://author-p106464-e993126.adobeaemcloud.com</td><td>https://publish-p106464-e993126.adobeaemcloud.com</td></tr><tr><td>L716058</td><td>https://author-p106520-e993236.adobeaemcloud.com</td><td>https://publish-p106520-e993236.adobeaemcloud.com</td></tr><tr><td>L716059</td><td>https://author-p106423-e993161.adobeaemcloud.com</td><td>https://publish-p106423-e993161.adobeaemcloud.com</td></tr><tr><td>L716060</td><td>https://author-p106516-e993078.adobeaemcloud.com</td><td>https://publish-p106516-e993078.adobeaemcloud.com</td></tr><tr><td>L716061</td><td>https://author-p106521-e993240.adobeaemcloud.com</td><td>https://publish-p106521-e993240.adobeaemcloud.com</td></tr><tr><td>L716062</td><td>https://author-p106424-e993308.adobeaemcloud.com</td><td>https://publish-p106424-e993308.adobeaemcloud.com</td></tr><tr><td>L716063</td><td>https://author-p106468-e993295.adobeaemcloud.com</td><td>https://publish-p106468-e993295.adobeaemcloud.com</td></tr><tr><td>L716064</td><td>https://author-p106425-e993309.adobeaemcloud.com</td><td>https://publish-p106425-e993309.adobeaemcloud.com</td></tr><tr><td>L716065</td><td>https://author-p106426-e993314.adobeaemcloud.com</td><td>https://publish-p106426-e993314.adobeaemcloud.com</td></tr><tr><td>L716066</td><td>https://author-p106469-e993293.adobeaemcloud.com</td><td>https://publish-p106469-e993293.adobeaemcloud.com</td></tr><tr><td>L716067</td><td>https://author-p106522-e993238.adobeaemcloud.com</td><td>https://publish-p106522-e993238.adobeaemcloud.com</td></tr><tr><td>L716068</td><td>https://author-p106470-e993299.adobeaemcloud.com</td><td>https://publish-p106470-e993299.adobeaemcloud.com</td></tr><tr><td>L716069</td><td>https://author-p106427-e993311.adobeaemcloud.com</td><td>https://publish-p106427-e993311.adobeaemcloud.com</td></tr><tr><td>L716070</td><td>https://author-p106428-e993310.adobeaemcloud.com</td><td>https://publish-p106428-e993310.adobeaemcloud.com</td></tr><tr><td>L716071</td><td>https://author-p106471-e993298.adobeaemcloud.com</td><td>https://publish-p106471-e993298.adobeaemcloud.com</td></tr><tr><td>L716072</td><td>https://author-p106429-e993315.adobeaemcloud.com</td><td>https://publish-p106429-e993315.adobeaemcloud.com</td></tr><tr><td>L716073</td><td>https://author-p106523-e993239.adobeaemcloud.com</td><td>https://publish-p106523-e993239.adobeaemcloud.com</td></tr><tr><td>L716074</td><td>https://author-p106472-e993300.adobeaemcloud.com</td><td>https://publish-p106472-e993300.adobeaemcloud.com</td></tr><tr><td>L716075</td><td>https://author-p106430-e993312.adobeaemcloud.com</td><td>https://publish-p106430-e993312.adobeaemcloud.com</td></tr><tr><td>L716076</td><td>https://author-p106524-e993241.adobeaemcloud.com</td><td>https://publish-p106524-e993241.adobeaemcloud.com</td></tr><tr><td>L716077</td><td>https://author-p106431-e993313.adobeaemcloud.com</td><td>https://publish-p106431-e993313.adobeaemcloud.com</td></tr><tr><td>L716078</td><td>https://author-p106473-e993294.adobeaemcloud.com</td><td>https://publish-p106473-e993294.adobeaemcloud.com</td></tr><tr><td>L716079</td><td>https://author-p106474-e993297.adobeaemcloud.com</td><td>https://publish-p106474-e993297.adobeaemcloud.com</td></tr><tr><td>L716080</td><td>https://author-p106475-e993296.adobeaemcloud.com</td><td>https://publish-p106475-e993296.adobeaemcloud.com</td></tr><tr><td>L716081</td><td>https://author-p106476-e993353.adobeaemcloud.com</td><td>https://publish-p106476-e993353.adobeaemcloud.com</td></tr><tr><td>L716082</td><td>https://author-p106525-e993247.adobeaemcloud.com</td><td>https://publish-p106525-e993247.adobeaemcloud.com</td></tr><tr><td>L716083</td><td>https://author-p106526-e993244.adobeaemcloud.com</td><td>https://publish-p106526-e993244.adobeaemcloud.com</td></tr><tr><td>L716084</td><td>https://author-p106527-e993243.adobeaemcloud.com</td><td>https://publish-p106527-e993243.adobeaemcloud.com</td></tr><tr><td>L716085</td><td>https://author-p106477-e993356.adobeaemcloud.com</td><td>https://publish-p106477-e993356.adobeaemcloud.com</td></tr><tr><td>L716086</td><td>https://author-p106478-e993355.adobeaemcloud.com</td><td>https://publish-p106478-e993355.adobeaemcloud.com</td></tr><tr><td>L716087</td><td>https://author-p106528-e993245.adobeaemcloud.com</td><td>https://publish-p106528-e993245.adobeaemcloud.com</td></tr><tr><td>L716088</td><td>https://author-p106432-e993316.adobeaemcloud.com</td><td>https://publish-p106432-e993316.adobeaemcloud.com</td></tr><tr><td>L716089</td><td>https://author-p106529-e993242.adobeaemcloud.com</td><td>https://publish-p106529-e993242.adobeaemcloud.com</td></tr><tr><td>L716090</td><td>https://author-p106436-e993320.adobeaemcloud.com</td><td>https://publish-p106436-e993320.adobeaemcloud.com</td></tr><tr><td>L716091</td><td>https://author-p106480-e993301.adobeaemcloud.com</td><td>https://publish-p106480-e993301.adobeaemcloud.com</td></tr><tr><td>L716092</td><td>https://author-p106530-e993246.adobeaemcloud.com</td><td>https://publish-p106530-e993246.adobeaemcloud.com</td></tr><tr><td>L716093</td><td>https://author-p106481-e993352.adobeaemcloud.com</td><td>https://publish-p106481-e993352.adobeaemcloud.com</td></tr><tr><td>L716094</td><td>https://author-p106482-e993354.adobeaemcloud.com</td><td>https://publish-p106482-e993354.adobeaemcloud.com</td></tr><tr><td>L716095</td><td>https://author-p106531-e993248.adobeaemcloud.com</td><td>https://publish-p106531-e993248.adobeaemcloud.com</td></tr><tr><td>L716096</td><td>https://author-p106483-e993357.adobeaemcloud.com</td><td>https://publish-p106483-e993357.adobeaemcloud.com</td></tr><tr><td>L716097</td><td>https://author-p106433-e993318.adobeaemcloud.com</td><td>https://publish-p106433-e993318.adobeaemcloud.com</td></tr><tr><td>L716098</td><td>https://author-p106532-e993249.adobeaemcloud.com</td><td>https://publish-p106532-e993249.adobeaemcloud.com</td></tr><tr><td>L716099</td><td>https://author-p106434-e993317.adobeaemcloud.com</td><td>https://publish-p106434-e993317.adobeaemcloud.com</td></tr><tr><td>L716100</td><td>https://author-p106435-e993319.adobeaemcloud.com</td><td>https://publish-p106435-e993319.adobeaemcloud.com</td></tr>
        </tbody>
</table>

+++

## Lesson 1

### Objective

Familiarize yourself with AEM Forms as a Cloud Service environment.

### Lesson context

In this lesson, you familiarize yourself with AEM Forms as a Cloud Service environment by navigating the user interface.

### Exercise

1.  Open your browser and enter the URL of the Cloud Service author environment.

1.  Log in to the Cloud Service author environment. The login credentials for your author environment are shared with you during the lab. 

1.  After you are logged in, navigate to the AEM Forms UI. Click **Forms**.

    ![](/help/forms/assets/screenshot2028113829.png)

1.  Click **Forms & Documents**. Dismiss any pop-ups related to preferences or information.

    ![](/help/forms/assets/screenshot2028113929.png)

    All the available forms are displayed.
    
    ![](/help/forms/assets/screenshot2028114029.png)

## Lesson 2

### Objective

Author an adaptive form using the latest core components, configure, and submit the form.

### Lesson context

In this lesson, as a business user, you will author an adaptive form for multiple channels like web, mobile, and chat using adaptive forms authoring with standardized OOTB core components for data capture.

### Exercise

1.  Create a submission endpoint for the form:

    1.  Open <https://requestbin.com/> in a new browser tab.
        ![](/help/forms/assets/screenshot2028114329.png)

    1.  Click **Create a public bin** and copy the endpoint URL.
        ![](/help/forms/assets/screenshot202023-03-0120at206.10.0020pm.png)

1.  Author an adaptive form using the Wizard interface:

    1.  In the browser tab used in Lesson 1, navigate to AEM Forms as Cloud Service web interface and navigate to Forms and Documents.
        ![](/help/forms/assets/screenshot2028114029.png)

    1.  Click **Create** and select Adaptive Form.
        ![](/help/forms/assets/screenshot2028114629.png)

    1.  Select the **Blank with Core Components** template from the template selection screen as shown below:
    ![](/help/forms/assets/screenshot202023-03-0120at206.09.1520pm.png)

    1.  Click the **Style** tab and select the **wknd-theme** theme as shown below:
    ![](/help/forms/assets/screenshot202023-03-0120at206.09.2320pm.png)

    1.  Click the **Submission** tab and select the **Submit to REST end-point** card and specify the public bin in the
    **URL for the POST request** field as shown below:
    ![](/help/forms/assets/screenshot202023-03-0120at206.09.5320pm.png)

    1.  Click **Create**. Specify a name and title to your form. For example, **contactus**. Click **Create**.
     ![](/help/forms/assets/screenshot2028123329.png)

    1.  The adaptive form editor opens. Dismiss any pop-ups or dialogs for preferences or information. Click the components browser on left rail and add the **Footer** component to the bottom of the blank form.
     ![](/help/forms/assets/screenshot2028121929.png)

    1.  The header is part of the adaptive form template. It allows an easy way to provide a consistent header/footer across all adaptive forms. Alternatively, you can also choose to keep it editable in the form - as seen for the Footer component in the next step.

    1.  Add a **Title** component to the middle of the form.
     ![](/help/forms/assets/screenshot2028122129.png)

    1.  Add a **Text Input** component after the title component.
     ![](/help/forms/assets/screenshot2028122329.png)

    1.  Add a **Number Input** component.
     ![](/help/forms/assets/screenshot2028122429.png)

    1.  Add a **Submit Button** component to the form.
     ![](/help/forms/assets/screenshot2028122529.png)

    1.  Click the **Title** component so that **pop-up menu** is displayed. Click the **Edit icon** in the menu to edit the label.
     ![](/help/forms/assets/screenshot2028122629.png)

    1.  Enter `Contact Us` as the title text.
    ![](/help/forms/assets/screenshot2028122829.png)

    1.  Click the **Text Input** component so that the pop-up menu is displayed. Click the **Edit icon** in the menu to edit the label.
    ![](/help/forms/assets/screenshot2028122929.png)

    1.  Enter **Full Name** as field label.
    ![](/help/forms/assets/screenshot2028123029.png)

    1.  Click the **Number Input** component so that the pop-up menu is displayed. Click the **Edit icon** in the menu to edit the label.
    ![](/help/forms/assets/screenshot2028123129.png)

    1.  Enter the **Phone number** as the field label.
    ![](/help/forms/assets/screenshot2028123829.png)


1.  Add validations to form:

    1.  Click the **Phone number** component so that the pop-up menu is displayed. Click the **Wrench icon** in the menu to configure the field.
        ![](/help/forms/assets/screenshot2028123429.png)

    1.  Open the **validations tab**, mark the field **Required**, and click **Done**. The success message is displayed.
        ![](/help/forms/assets/screenshot2028123529.png)
        
        ![](/help/forms/assets/screenshot2028123629.png)

    1.  Click **Preview** to preview the form from an end-user perspective.
        ![](/help/forms/assets/screenshot2028125529.png)

    1.  Fill the form with dummy data
        ![](/help/forms/assets/screenshot2028125629.png)

    1.  Submit the form
        ![](/help/forms/assets/screenshot2028125729.png)

    1.  In the Request bin tab, check the submitted data.
        ![](/help/forms/assets/screenshot2028125829.png)

Now for purpose of the remaining exercise, use a pre-created registration form.

1.  Open AEM Forms management interface, for example, `https://author-p105303-e986623.adobeaemcloud.com/ui%23/aem/aem/forms.html/content/dam/formsanddocuments`, and select the registration form.
    
    ![](/help/forms/assets/screenshot2028115529.png)

1.  Click **Publish**.

    ![](/help/forms/assets/screenshot2028115629.png)
    
    The success message is displayed.

    ![](/help/forms/assets/screenshot2028115729.png)

    The publish URL of the form would be similar to `https://publish-p105303-e986623.adobeaemcloud.com/content/forms/af/registration.html`.

1.  To view the published form replace the program ID (pXXXXXX) and environment ID (eXXXXXX) in the above URL with ID's of your
    environment.

## Lesson 3

### Objective

Update styles using frontend development best practices.

### Lesson context

In this lesson, as a front-end developer, you learn how you can update styling for the previously created adaptive form easily.

### Exercise

Set up local repository of the theme:

1.  Open the Command Prompt or shell with administrator rights:

    ![](/help/forms/assets/screenshot2028115829.png)

1.  On the Command Prompt, use the following command to navigate to **c:\git** folder
    
    ```Shell
    
    cd c:\git
    
    ```

1.  Use the following command to clone the theme frontend code:
    
    ```Shell
    
    git clone -b WKND https://github.com/adobe/aem-forms-theme-canvas

    ```
    

1.  Use the following command in the listed order to navigate to the **aem-forms-theme-canvas** directory and open Visual Studio Code.
    
    ```Shell
    
    cd aem-forms-theme-canvas
    code .

    ```
    
    ![](/help/forms/assets/screenshot2028126029.png)

1.  Select **Trust the authors of all files in the parent folder** and click **Yes, I trust the authors**.

    ![](/help/forms/assets/screenshot2028116229.png)

1.  To render the form hosted on your cloud service publish environment, rename the `env_template` file.  To rename the file, right-click the **env_template** file and select the **Rename** option.

    ![](/help/forms/assets/screenshot2028116429.png)

     </br>

    ![](/help/forms/assets/screenshot2028116529.png)

1.  Set the following values for the variables in .env file and save the file:

    *   **AEM_URL**: Specify your cloud service publish environment. For example, `https://publish-p105303-e986623.adobeaemcloud.com/`
    
    *   **AEM_ADAPTIVE_FORM**: Specify the path of the form. For example, if the form path is `/content/forms/af/registration`, the value of this variable would be `registration`.

    ![](/help/forms/assets/screenshot2028116429.png)
    

1.  In the Command Prompt window, run the following command:

    ```Shell

    npm install

    ```

    ![](/help/forms/assets/screenshot2028117029.png)

    >[!NOTE]
    >
    > * If you get a message asking to update npm via the `npm notice Run npm nstall -g npm@9.6.0`command, ignore the message.
    > * Do not run other npm commands unless instructed in the workbook.

1.  Now run the following command to preview the form.
    
    ```Shell
    
    npm run live
    
    ```
    
    ![](/help/forms/assets/screenshot2028117229.png)

    Once the above command is executed, wait for the `webpack compiled` message. The form is displayed in a browser tab.

    >[!NOTE]
    >
    >If you experience a blank screen in browser after executing the `npm run live` command for more than 3-4 minutes, change `localhost` in browser URL to 127.0.0.1 and hit **Enter**. 

    
    ![](/help/forms/assets/screenshot2028115129.png)


1.  In Visual Studio Code, open the `PROJECT\src\site\_variables.scss` file. Notice the `$error` color is a shade of RED.

    ![](/help/forms/assets/screenshot2028120729.png)

1.  In the browser, submit the form to see the Red color in the **First Name** field.

    ![](/help/forms/assets/screenshot2028120829.png)

1.  Set the **$error** color to **#5736eb** and save the file. 

    ![](/help/forms/assets/screenshot2028120729.png)

1.  Refresh the browser and submit the form. Notice error color on the first name field has changed accordingly.
    
    ![](/help/forms/assets/screenshot2028121129.png)

1.  In the Command Prompt, press **CTRL+C**, enter **Y**, and press **Enter** key to terminate the npm process. It is important to stop the npm server so it does not conflict with the next set of exercises.
1.  Close Visual Studio Code and Command Prompt windows.

## Lesson 4

### Objective

Render the form to web/mobile and other interfaces as a headless form.

### Lesson context

In this lesson, as a frontend developer, you will learn how you can render the adaptive form created previously as a headless form using react spectrum design framework.

### Exercise

Setup local repository using react starter project:

1.  Open the Command Prompt using administrator rights.

    ![](/help/forms/assets/screenshot2028115829.png)

1.  On the Command Prompt, use the following command to navigate to **c:\git** folder

    ```Shell
    
    cd c:\git

    ```

1.  Use the following command to clone the adaptive form react starter project:
    
    ```Shell
    
    git clone https://github.com/adobe/react-starter-kit-aem-headless-forms

    ```
    
    ![](/help/forms/assets/screenshot2028117329.png)

1.  Use the following commands in the listed order to navigate to the **react-starter-kit-aem-headless-forms** directory and open Visual Studio Code.

    ```Shell
    
    cd react-starter-kit-aem-headless-forms

    code .

    ```
    
    ![](/help/forms/assets/screenshot2028117529.png)
    

    The Visual Studio Code window opens.

    ![](/help/forms/assets/screenshot2028117429.png)

To render the form hosted on your cloud service publish environment:

1.  Rename the env_template file to .env file. To rename, right-click the **env_template** file and select the **Rename** option. 
    
    ![](/help/forms/assets/screenshot2028117629.png)
    
    ![](/help/forms/assets/screenshot2028117729.png)

1.  Set the following values for the variables in the .env file. After updating variables, save the file.

    *   **AEM_URL**: Specify the URL of the cloud service publish environment. For example, `https://publish-p105303-e986623.adobeaemcloud.com`

    *   **AEM_FORM_PATH**: Specify the path of the adaptive form created in the previous lesson. For example, `/content/forms/af/registration/`

        ![](/help/forms/assets/screenshot202023-03-0820at202.49.1820pm.png)

1.  Open the command window, ensure you are at the react-starter-kit-aem-headless-forms directory, and run the following command:

    ```Shell
    
    npm install
    
    ```

    ![](/help/forms/assets/screenshot2028118029.png)


1.  In the Command Prompt window, run the following command:
    
    ```Shell

    npm start
    
    ```

    ![](/help/forms/assets/screenshot2028118129.png)

    The above command starts a local development server which would render the form definition fetched from AEM in a headless way using the react-spectrum frontend library.

    >[!NOTE]
    >
    > 
    > If you experience a blank screen in browser after executing the `npm start` command for more than 3-4 minutes, change `localhost` in browser URL to 127.0.0.1 and hit **Enter**. 

    ![](/help/forms/assets/screenshot2028118229.png)

Let's check the execution of rules in this headless form:

1.  Select the **Check the box to receive 5% off** option. The subsequent option for applying credit card is disabled.

    ![](/help/forms/assets/screenshot2028126229.png)

1.  Uncheck **Check the box to receive 5% off** to enable the credit card option.

    ![](/help/forms/assets/screenshot2028126329.png)

Let's make changes on the form on the server as a business user and view changes reflected in the headless form automatically.

1.  Open the AEM Forms management interface in the browser.
\
1.  Select the **registration** form and click **Edit.** It opens the form in the adaptive forms editor.

    ![](/help/forms/assets/screenshot2028118529.png)

1.  Select the **Phone number** field and click the **Edit icon (Pencil icon)** in the toolbar. If you are not able to see the pop up toolbar, switch to Edit mode by clicking **Edit** button in top right, left to **Preview** button.

    ![](/help/forms/assets/screenshot2028119629.png)

1.  Change the label to Mobile Number. Click any empty space in the form and the changes made to the form are saved.

      ![](/help/forms/assets/screenshot2028119729.png)

Let's publish the updated form to propagate the changes to publish environment.

1.  In the AEM Forms management interface tab, select the registration form, and click **Unpublish**. If you do not see the **Unpublish** button, skip to step 3 to publish the changes directly.

      ![](/help/forms/assets/screenshot2028119829.png)

1.  Click **Unpublish**. Click **Close** in respective dialog.
    
    ![](/help/forms/assets/screenshot2028119929.png)

    ![](/help/forms/assets/screenshot2028120029.png)


1.  After the browser refreshes, select the registration form and click **Publish**.

    ![](/help/forms/assets/screenshot2028120129.png)


1.  Click **Publish**. Click **Close** in the respective dialog.

    ![](/help/forms/assets/screenshot2028120329.png)
    
    ![](/help/forms/assets/screenshot2028120429.png)

1.  Refresh the browser tab with the headless form displayed. Notice, the Phone number label has changed to Mobile number.

    ![](/help/forms/assets/screenshot2028120529.png)

1.  Open the Command Prompt window that is used to start the **react-starter-kit-aem-headless-forms** project, press **CTRL+C**, then
    enter **Y** and press Enter key to terminate the npm process. It is important to stop the npm server so it does not conflict with the next set of exercises.

1.  Close Visual Studio Code and Command Prompt windows.


## Lesson 5

### Objective

Render the form as a headless form using Google Material UI

### Lesson context

In this lesson, as a front-end developer, you learn how to render the adaptive form created previously as a headless form using Google Material UI.

### Exercise

Setup local repository using Material UI starter project:

1.  Open the Command Prompt using administrator rights.
    
    ![](/help/forms/assets/screenshot2028115829.png)


1.  On the Command Prompt, use the following command to navigate to **c:\git** folder:

    ```Shell

    cd c:\git

    ```

1.  Run the following commands in the listed order to create a folder named mui and navigate to the mui folder using following commands: 

    ```Shell

    mkdir mui

    cd mui
    
    ```

1.  Use the following command to clone the adaptive form react starter project: 

    ```Shell

    git clone -b mui https://github.com/adobe/react-starter-kit-aem-headless-forms

    ```

    ![](/help/forms/assets/screenshot2028126529.png)

1.  Use the following command in the listed order to navigate to the **react-starter-kit-aem-headless-forms** folder and open the code in Visual Studio Code:

    ```Shell

    cd react-starter-kit-aem-headless-forms

    code .

    ```

    ![](/help/forms/assets/screenshot2028126829.png)

To render the form hosted on your cloud service publish environment:

1.  Rename the **env_template** file to **.env** file. To rename, right-click the **env_template** file and select **Rename**.

    ![](/help/forms/assets/screenshot2028126629.png)

1.  Set the following values for the variables in the .env file. After updating variables, save the file. Use the **CTRL + S** switch combination to save the file. 

    *   **AEM_URL**: Specify the URL of the cloud service publish environment.

    *   **AEM_FORM_PATH**: Specify the path of the adaptive form created in the previous lesson. For example, /content/forms/af/registration/

        ![](/help/forms/assets/screenshot2028126929.png) 

1.  Open the command window, ensure you are at the **react-starter-kit-aem-headless-forms** directory, and run the following command:

    ```Shell
    
    npm install
    
    ```

    ![](/help/forms/assets/screenshot2028127029.png)

1.  In the Command Prompt window, run the following command:
    
    ```Shell

    npm start
    
    ```

    ![](/help/forms/assets/screenshot2028127129.png)
    
    The command starts a local development server and renders the form definition fetched from AEM in a headless way using the Google
    Material UI frontend library.

    >[!NOTE]
    >
    >If you experience a blank screen in browser after executing the `npm start` command for more than 3-4 minutes, change `localhost` in browser URL to 127.0.0.1 and hit **Enter**. 

    ![](/help/forms/assets/screenshot2028127229.png)

1.  To evaluate the execution of the same business logic in this form rendition: 

    Select **Check the box to receive 5% off**. The subsequent option **Would you like to apply for We.Finance Corporate Credit Card Form?** gets disabled.

    ![](/help/forms/assets/screenshot2028127329.png)

## Lesson 6

### Objective

Create an alternate look and feel of the headless form using Material UI component variations

### Lesson context

In this lesson, as a front-end developer, you learn how to create an alternate representation of different components using Material UI for the adaptive form created previously by the business user.

### Exercise

Update the variation of components in the headless project. To change the variant of the material UI text input component to `OutlinedInput`: 

1.  In Visual Code, navigate to the text input component by opening the `index.tsx` file at `src/components/textinput/index.tsx`.

1.  Add `//` at the beginning of the code line 103. It converts the line to a comment. 

    ```Shell

    //const Cmp = \'outlined\' === appliedCssClassNames ? OutlinedInput: Input;

    ```

1.  Add the following at line 104 to use a different variant of component and save the file. Use the **CTRL + S** switch combination to save the file. 

    ```Shell
    
    const Cmp = OutlinedInput;

    ```

    ![](/help/forms/assets/screenshot2028127629.png)

    It is essential to use correct capitalization for 'OutlinedInput' variant else compilation would fail. The local development environment compilation begins automatically in Command Prompt. Wait until you see the following message

    `webpack 5.75.0 compiled with 3 warnings in 6659 ms` 
    `inside proxy req`
    `setting new origin header`

1.  Refresh the browser, if it does not refresh automatically, to see text input component use a different variant.

    ![](/help/forms/assets/screenshot2028127729.png)

    
    This change happens for end users without any change to form definition at AEM Forms Server and is specific for the headless
    channel under consideration. For example, web channel in this lab.
    
    ![](/help/forms/assets/screenshot2028127529.png)


1.  Close Visual Studio Code and Command Prompt Windows.

## Frequently Asked Questions (FAQs)

+++ Is Adaptive Form wizard available publicly?  

Yes, it available with AEM Forms as Cloud Service.

+++


+++ Are core components available publicly?  

Yes, Adaptive Forms core components are available with AEM Forms as Cloud Service.

+++

+++ Are Headless forms available publicly?  

Yes, Headless forms are available with AEM Forms as Cloud Service.

+++

+++ Do Headless forms require a separate license?  

No, Headless forms use the same licensing value metric, number of form submissions.

+++

+++ Are Core components and Headless forms available with AEM 6.5 Forms?  

Yes, both adaptive forms core components and headless forms are available with AEM Forms 6.5 Service Pack 16 and onwards. 

+++


## Next steps

Now that you have learned how to build adaptive forms and deliver them to multiple channels using headless forms, you should try to put your new skills in action. Have fun and go ahead by creating and delivering exceptional data capture experiences to your end users, where they are, at scale!

## Resources

*   [Adaptive Form core components introduction](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html)

*   [Create adaptive form using core components](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/creating-adaptive-form-core-components.html)

*   [Update styling for core component-based AF](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/using-themes-in-core-components.html?lang=en)

*   [Headless adaptive forms](https://experienceleague.adobe.com/docs/experience-manager-headless-adaptive-forms/using/overview.html?lang=en)

*   [Using Headless React starter kit](https://experienceleague.adobe.com/docs/experience-manager-headless-adaptive-forms/using/get-started/create-and-publish-a-headless-form.html?lang=en)
