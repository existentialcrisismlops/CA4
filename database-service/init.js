// init.js
// Script to initialize MongoDB collections and insert data

// Import the MongoDB Node.js driver
const { MongoClient } = require('mongodb');

// MongoDB connection URL
const url = 'mongodb://localhost:27017';

// Database name
const dbName = 'my_database';

// MongoDB client
const client = new MongoClient(url);

// Data initialization function
async function initializeData() {
  try {
    await client.connect();
    const db = client.db(dbName);

    const usersCollection = db.collection('users');
    await usersCollection.insertMany([
      { name: 'User1', email: 'user1@example.com' },
      { name: 'User2', email: 'user2@example.com' },
    ]);

    console.log('Data initialization complete.');
  } catch (error) {
    console.error('Error initializing data:', error);
  } finally {
    // Close the MongoDB connection
    client.close();
  }
}

initializeData();
