
function randomNumber(min, max) { 
    return (Math.random() * (max - min) + min);
} 


async function getter(params,url)
{
    const response = await fetch(url,params);
    const label = await response.json();
    return label;

}

async function predictor()
{
    campaign_dict = {0:'Other',1:'Shoes Sale-Display Ads',2:'Seach Ads-Summer-Shoes',3:'Dynamic Search Ads-Shoes',4:'Father day shoes sale-Display ads'};
    device_category_dict = {0:'tablet',1:'desktop',2:'mobile'}
    social_network_dict = {0:'Other',1:'Facebook',2:'Instagram Stories',3:'Slashdot',4:'Twitter',5:'LinkedIn',6:'Yelp',7:'Quora'}
    var Data = {
         avg_session_duration : randomNumber(0,7000),
         campaign : campaign_dict[int(randomNumber(0,4))],
         hits : int(randomNumber(10,7600)),
         day_of_week : int(randomNumber(0,6)),
         day : int(randomNumber(1,31)),
         device_category : device_category_dict[int(randomNumber(0,2))],
         entrances : int(randomNumber(0,450)),
         events_per_session : randomNumber(0,400),
         exits : int(randomNumber(0,450)),
         hour : int(randomNumber(0,24)),
         organic_search : int(randomNumber(0,10)),
         page_depth : int(randomNumber(0,500)),
         page_views : int(randomNumber(1,5600)),
         page_views_per_session : randomNumber(1,450),
         sessions : int(randomNumber(1,450)),
         social_network : int(randomNumber(0,7)),
         events : int(randomNumber(1,2000)),
         unique_events : int(randomNumber(1,600)),
         week : int(randomNumber(20,40)),
         frequency : int(randomNumber(1,20)),
    };
  const url = '';
  const params = {
      body:JSON.strinify(Data),
      method:'POST',
      headers : {
        'Content-Type': 'application/json',
      },
  }
  await getter(params,url).then(label => {
    console.log(label);
  });

}