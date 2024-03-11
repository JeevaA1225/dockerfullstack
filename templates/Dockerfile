# Use a lightweight web server image
FROM nginx:alpine

# Copy static files to Nginx directory
COPY ./ /usr/share/nginx/html

# Expose port
EXPOSE 80

# Command to run the service
CMD ["nginx", "-g", "daemon off;"]
