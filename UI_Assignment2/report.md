[TOC]

# Assignment 2: Information Retrieval

## Interface Preview

### Home Page

![image-20210603144201387](report.assets/image-20210603144201387.png)

### Tag

![image-20210603165740690](report.assets/image-20210603165740690.png)

### Preview & Searching

![image-20210603100810211](report.assets/image-20210603100810211.png)

### Results

![image-20210603100840021](report.assets/image-20210603100840021.png)

### Favorites

![image-20210603101956204](report.assets/image-20210603101956204.png)



## Manual

1. Click "Home" to refresh the page and return to the home page.

   ![Home](report.assets/Home.gif)

2. Click "Tag" to turn to the Tag Section.

   ![Tag](report.assets/Tag.gif)

3. Click "Favorites" to turn to the Favorites Section.

   ![Favorites](report.assets/Favorites.gif)

4. Choose zero or more tags to filter the images before searching.

   ![tags](report.assets/tags.gif)

5. Click the "Get Started" button to upload your file.

   ![upload](report.assets/upload.gif)

6. Click the "Search" button to start searching.
   ![search](report.assets/search.gif)

7. Choose zero or more tags to filter the result images.

   ![retags](report.assets/retags.gif)

8. Click the "Clear" button to clear the results.

   ![clr](report.assets/clr.gif)

9. Click the star icon to add images into or remove images from your favorites.

   ![fav](report.assets/fav.gif)



## Requirements of an Image Search Task

**Basic**

1. A clear and concise interface with some pre-suggestions.
2. An input box for inputing key words or uploading images with preview.
3. A search button to execute searching.
4. Provide an overview (total number).
5. Be able to display the searching results with a brief description.
6. Be able to search by additional conditions (color,type...).
7. Be able to zoom in to see the images and save.

**More**

1. Varieties of search method (phonetic search).
2. Input with help of auto-completion.
3. Categorize results using metadata.
4. Allow adjustment of the size of the result set.
5. Allow change of sequencing (alphabetical, chronological, relevance ranked, etc).
6. Provide related searches of the result set.
7. Explore collecting explicit feedback (ratings, reviews, like, etc).

## Designs for Five Stages

### Formulation

![image-20210603160102091](report.assets/image-20210603160102091.png)

1. Provide an input box for uploading images.
2. After an image was uploaded, a preview will be shown.

### Initiation

![image-20210603160513682](report.assets/image-20210603160513682.png)

1. When the search button is clicked, the searching process starts.

### Review

![image-20210603163546537](report.assets/image-20210603163546537.png)

1. Keep search terms and constrains visible.
2. Provide an overview of results (total number).
3. Provide descriptive previews of each result item.

### Refinement

![image-20210603164018933](report.assets/image-20210603164018933.png)

1. Allow changing search parameters (select certain tag) when reviewing results.

### Use

![image-20210603164544843](report.assets/image-20210603164544843.png)

1. Allow adding/removing selected images to/from a favorite list.

## How to run

Environment: python 3.8.8

1. Decompress the file.
2. Install the concerned packages if needed.
3. Change the directory to "lab2-image-retrieval" and move the local folder "database" into "lab2-image-retrieval/server".
4. Terminal run: python rest-server.py.