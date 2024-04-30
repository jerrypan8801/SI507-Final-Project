Champion Network Project

Description:
This project implements a ChampionNetwork using game data (League Of Legends) to analyze and visualize relationships between champions in a network graph. The network graph connects champions who appear together in games, and these connections are weighted by their co-occurrence frequency.

Features:
- Interactive menu to explore different network insights:
  1. Query specific champions to see their connections with other champions.
  2. Display the most common champion pairs.
  3. List the most influential champions based on network centrality.
  4. Identify isolated champions within the network.

User Interaction Features:
The application offers a robust command-line interface that empowers users to deeply engage with the network data of champions through various insightful functionalities:
- Detailed Champion Insights: Users can input the ID of a champion to access comprehensive details about their connections, enhancing understanding of their roles and interactions within the network.
- Champion Pair Analysis: The interface allows users to view and analyze the top pairs of champions that frequently collaborate, providing insights into common alliances and strategies.
- Influence Exploration: Users can explore the network to identify champions with the highest influence, revealing key players and central figures in the network graph.
- Isolation Detection: The application also enables users to discover champions who are isolated or have minimal connections, highlighting potential outliers or underutilized champions.

Technical Specifications:
- Required Python Packages:
  - pandas: For data manipulation and analysis.
  - networkx: For creating and manipulating the network graph.

- Data Files:
  - games.csv: Contains the game (champions) data used to construct the graph.


Setup Instructions:
1. Ensure Python is installed along with the pandas and networkx libraries.
2. Download the games.csv data file and place it in the project directory.
3. Run the script from your command line or IDE.

End User Documentation:
- Starting the Program: Launch the program by executing the Python script. You can do this from your command line or through your IDE.
- Interactive Prompts: After starting the application, follow the on-screen prompts to navigate through the network analysis features. The interface is designed to guide you through each step for a seamless user experience.
- Exiting the Application: At any point, if you wish to exit the application, simply input 'q' and press enter. This command will safely close the application and end the session.