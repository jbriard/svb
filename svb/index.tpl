<!DOCTYPE html>
<html><head>
  <title>
Scaleway - Container
  </title>
  <meta charset="utf-8">
  <meta name="author" content="Justin Briard" />
  <meta name="description" content="Kubernetes Demo pod">


<style>


body {
    background-color: rgb(255, 255, 255);
    color: rgb(74, 79, 98);
    font-family: Asap, -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 0.8rem;
    height: 100%;
    margin: 10px;
}

footer {
    background-color: rgb(255, 255, 255);
    color: rgb(74, 79, 98);
    font-family: Asap, -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 0.5rem;
    height: 100%;
    margin: 0px;
    display: flex;
    justify-content: center;
    padding: 5px;
    background-color: rgb(242, 242, 242);

}

</style>

    </head>
<body>
    
<center><a href="https://scaleway.com" alt="link to scaleway web site"><img src="/static/Logotype_Scaleway_Purple.png" alt="Logo Scaleway"</i></a></center>
<br />


<center><img src="/static/{{!BADGE}}" alt="Valeurs Scaleway" width="310" </i></center>

<p> 
  <pre>
  NODE_NAME: {{!MY_NODE_NAME}}
  POD_NAME: {{!MY_POD_NAME}}
  POD_NAMESPACE: {{!MY_POD_NAMESPACE}}
  POD_IP: {{!MY_POD_IP}}
  CONTAINER_ID: {{!MY_CONTAINER_ID}}
 </pre> 
</p>

<!-- looking for a Job ? Scaleway is hiring https://careers.scaleway.com/ -->

</body>

</html>
