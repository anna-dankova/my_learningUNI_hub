import sqlite3

conn = sqlite3.connect('data/wardrobe.db')
conn.execute("UPDATE garments SET image_path = REPLACE(image_path, 'raw_images', 'processed_images')")
conn.commit()
print('Done — пути обновлены:')
rows = conn.execute('SELECT id, image_path FROM garments').fetchall()
for r in rows:
    print(r)
conn.close()
