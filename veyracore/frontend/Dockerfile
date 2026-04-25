FROM node:22-alpine

WORKDIR /app

# Copy package files
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm ci --only=production 2>/dev/null || npm install --only=production

# Copy application code
COPY . .

# Build Next.js application
RUN npm run build

# Expose port
EXPOSE 3000

# Set environment for production
ENV NODE_ENV=production

# Run the application
CMD ["npm", "start"]
