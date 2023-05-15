# Use an official Node.js runtime as the base image
FROM node:18-alpine as build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package.json package-lock.json ./

# Install dependencies
RUN npm i

# Copy the remaining application files to the container
COPY . .

# Build the application
RUN npm run build

# Use a smaller lightweight base image for production
FROM nginx:alpine

# Copy the built files from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose the default HTTP port
EXPOSE 80

# Start the Nginx server
# CMD ["nginx", "-g", "daemon off;"]