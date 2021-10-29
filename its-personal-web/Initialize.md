# How to initialize the Vue multi page project and deploy to Heroku

Table of contents:
1. Install a Node Version Manager
2. Initialize a new Vue project
3. Refactor from Single Page Application (SPA) to Multi Page Application (MPA)
4. Deploy to Heroku

## Install a Node Version Manager for Node.js
### Windows
[Github repository for nvm-windows](https://github.com/coreybutler/nvm-windows)

- Uninstall existing node and npm (generally found in `ProgramFiles\nodejs` and in `C:\Users\<username>\AppData\Roaming\npm`). Alternatively can also search for the uninstaller program.
- Download the latest installer [here](https://github.com/coreybutler/nvm-windows/releases) (The `nvm-setup.zip` file)
- Unpack the zipfile and run the installer.

### Mac/Linux
[Github repository for nvm](https://github.com/nvm-sh/nvm)

### How to use:
### Install latest npm
```sh
nvm install latest
```
### Check instaled npm
```sh
nvm list
```
### Use installed npm version
```sh
nvm use <version number>
```
### Check current npm version
```sh
npm -v
```
### Uninstall npm version
```sh
nvm uninstall <version number>
``` 

## Initialize a New Vue Project
[Official Vue documentation](https://cli.vuejs.org/guide/installation.html)
### Install Vue
```sh
npm install -g @vue/cli
```
### Check Vue version
```sh
vue --version
```
### Create new project
```sh
vue create <project-name>
```
When prompted, choose the default Vue 3 preset.
### Move to the new repository
```sh
cd <project-name>
```
The current project is a single page application that shows the initial template for a webpage. The following commands are scripts that written in the `package.json` file.
### Run the project
```sh
npm run serve
```
The website will be viewable in `localhost:8080` by default.
### Build the project
```sh
npm run build
```
This command is mainly used in the production/deployment phase and will generate a build folder.
### Check for mistakes in the project files
```sh
npm run lint
```
### Simulate the production environment for running the project
```sh
npm run production
```
Simulates using the build file to serve the website. Prerequisite: Must add the following to the `scripts` section in the `package.json` file:
```json
"production": "vue-cli-service serve --mode production"
```

## Refactor from SPA to MPA
The initial template given by Vue is made for Single Page Applications or in other words single page websites. Since we want to have multiple pages, we need to change it to accomodate Multi Page Applications. Adapted from the [stackoverflow answer here](https://stackoverflow.com/questions/51692018/multiple-pages-in-vue-js-cli)
1. Create a new `pages` folder under `src`.
2. Create a new folder for each page we want under `pages`. The new folders are `home`, `login`, and `about`.
3. Move and copy the `App.vue` and `main.js` files that were located under `src` to each of the new page folders. Make some changes in the `App.vue` file to mark the difference between the pages.
4. Adjust the paths in the `App.vue` files to point in the right directory (in our case just changed `./` to `../../`)
5. Create a new file called vue.config.js containing the following:
```js
module.exports = {
    pages: {
        'index': {
            entry: './src/pages/home/main.js',
            template: 'public/index.html',
            title: 'home',
            chunks: [ 'chunk-vendors', 'chunk-common', 'index' ]
        },
        'about': {
            entry: './src/pages/about/main.js',
            template: 'public/index.html',
            filename: 'about.html',
            title: 'about',
            chunks: [ 'chunk-vendors', 'chunk-common', 'about' ]
        },
        'login': {
            entry: './src/pages/login/main.js',
            template: 'public/index.html',
            filename: 'login.html',
            title: 'login',
            chunks: [ 'chunk-vendors', 'chunk-common', 'login' ]
        }
    }
}
```
6. The pages will now be viewable when running `npm run serve`. The urls are `/about.html`, `/login.html`, and anything else will show the `index` page.

## Deploy the Vue Project to Heroku
Adapted from the [guide available here](https://dev.to/anjolaogunmefun/deploy-vue-js-projects-to-heroku-1hb5)
### Install express and serve-static
```sh
npm install express serve-static
```
### Create a new file called `server.js`
The content of the file should be as follows:
```js
const express = require('express');
const serveStatic = require("serve-static")
const path = require('path');
app = express();
app.use(serveStatic(path.join(__dirname, 'dist')));
const port = process.env.PORT || 3000;
app.listen(port);
```
### Add new scripts in `package.json`
The new scripts are as follows:
```json
"postinstall": "npm run build",
"start": "node server.js"
```
### Create a new Github repository
Use the normal method of creating a new repository in Github. After that run the following in the Vue project directory:
```sh
git init
git add .
git commit -m "Initialize Vue project"
git remote add origin <github repository url>
git push origin master
```
### Create a new Heroku application
Use the normal method of creating a new Heroku application. In the deploy page, select the Github deployment method. After that, choose the Enable Automatic Deploys option. Authorize Heroku using the github account for the repository, then select the repository and branch, then deploy. Access the deployed website from the generated View button, or select the Open app button.