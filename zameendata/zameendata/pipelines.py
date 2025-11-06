from pymongo import MongoClient

class MongoDBPipeline:
    def open_spider(self, spider):
        # Connect to MongoDB Atlas
        self.client = MongoClient("mongodb+srv://<db_name>:<db_password>@cluster0.uq8my.mongodb.net/") # >> replace with your atlas credentials
        self.db = self.client["zameen_database-1"]
        self.collection = self.db["zameen_listings"]

        # Create an empty buffer list
        self.items_buffer = []
        spider.logger.info(" Connected to MongoDB Atlas")

    def process_item(self, item, spider):
        # Add each scraped item to buffer
        self.items_buffer.append(dict(item))

        # When buffer reaches 100 items, insert all at once
        if len(self.items_buffer) >= 5:
            try:
                self.collection.insert_many(self.items_buffer)
                spider.logger.info(f"🚀 Inserted {len(self.items_buffer)} items (batch insert)")
                self.items_buffer.clear()  # Empty the buffer
            except Exception as e:
                spider.logger.warning(f"❌ Batch insert error: {e}")

        return item

    def close_spider(self, spider):
        # If any items are left in the buffer, insert them too
        if self.items_buffer:
            try:
                self.collection.insert_many(self.items_buffer)
                spider.logger.info(f"💾 Inserted remaining {len(self.items_buffer)} items before closing")
            except Exception as e:
                spider.logger.warning(f"❌ Final insert error: {e}")

        self.client.close()
        spider.logger.info("🔒 MongoDB connection closed")
