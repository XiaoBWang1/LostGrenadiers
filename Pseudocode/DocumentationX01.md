Blueprint Code/Algorithm Documentation 01
Python(PyCharm)/Leaflet/Folium 
	
	Pre-App
	Application is activated by user 		
	clicking on the Lost Grenadiers' logo icon 
 	and then the user is connected to the
	server/database and is granted access to 
 	either a main OSD(on-screen display) of the logo or 
	directly directs the user to start their 
	search task of the IUS' campus. The end user is 
	graphically marked/start at Life Science building at X and Y 
	coordinates or be prompt to fill certain 
	field/form/filter to streamline the process. 
	
	Main OSD
	The user is either prompted a vague question||fixated on 
	a map marker||located with their current 
	coordinates(GPS)||shown a login screen(Google/Apple/etc). Then 
	the prompt will appear asking the 		   
 	user for their input to certain field/attributes/
  	characteristics. The inputted data will eliminate 
   	all the applicable outputs retrieved from the database 
	locally/Internet(web). The 
	outputted data will be presented to the 
	user and awaits their response on what 	
	task should be executed(another search 
	query/exit/refine previous search).  

	import library/packages
	//import folium	
	//import pandas as pd
	
	start map centered on a fixed 	
	position of IUS
	//IUS_coordinates = []
	
	instantiate the map on display
	//IUS_map = 

	on-screen map of Life Science(IUS)
	//IUS_map	
	
	Interrupt session with a search menu 
	that filters out different entities within
	the data, then the marker will move 
	toward the appropriate 				   
	location(building) and zoom toward to
	the correct output if the search was 
	error free && applicable && data available.
 	Then the associated text/image data that's available will
	be shown to the user through the API, then the user  
	decides whether to refine/reuse the 
 	search function||end their access||stay 
	status quo in the background. 
	
	
	
		
	
	
	
