import java.util.*;

 class MyMap<K extends Object,V extends Object> {

    private ArrayList<LinkedList<MyMap.Entry<K,V>>> bucketList;
    private int size;

    public MyMap(int size) {
      this.size = size;
      bucketList = new ArrayList<>();

      for (int i = 0; i < size; i++) {
        LinkedList<MyMap.Entry<K,V>> ll = new LinkedList<>();
        bucketList.add(ll);
      }

    }

    // Implements put() of a hashmap
    public void put(K key, V value) {
      if (key == null) {
        return;
      }

      int hash = hash(key);
      MyMap.Entry<K, V> newEntry = new MyMap.Entry<K, V>(key, value);
      LinkedList<Entry<K,V>> linkedList = bucketList.get(hash);

      if (linkedList.size() == 0) {
        linkedList = bucketList.get(hash);
        linkedList.add(newEntry);
      } else {
        for (MyMap.Entry<K,V> entry: linkedList) {
            K entryKey = entry.getKey();
            if (entryKey.equals(key)) {
              entry.setValue(value);
              return;
            }
        }

        linkedList.add(newEntry);
      }

    }

    // Implements get() of a hashmap
    public V get(K key) {
      int hash = hash(key);

      LinkedList<Entry<K,V>> linkedList = bucketList.get(hash);

      if (linkedList.size() == 0) {
        return null;
      } else {
        for (MyMap.Entry<K,V> entry: linkedList) {
            K entryKey = entry.getKey();
            if (entryKey.equals(key)) {
              return entry.getValue();
            }
          }
        }
      return null;
    }

    // Remove a key-value pair from the hashmap
    public V remove(K key) {
      if (key == null) {
        return null;
      }

      int hash = hash(key);

      LinkedList<Entry<K,V>> linkedList = bucketList.get(hash);
      MyMap.Entry<K,V> removeEntry = null;

      if (linkedList.size() == 0) {
        return null;
      } else {
        for (MyMap.Entry<K,V> entry: linkedList) {
          if (entry.getKey().equals(key)) {
            removeEntry = entry;
          }
        }
      }

      if (removeEntry != null) {
        linkedList.remove(removeEntry);
        return removeEntry.getValue();
      }

      return null;
    }

    // Checks if a key is present in a hashmap
    public boolean containsKey(K key) {
      if (key == null) {
        return false;
      }

      int hash = hash(key);
      LinkedList<Entry<K,V>> linkedList = bucketList.get(hash);

      if (linkedList.size() == 0) {
        return false;
      } else {
        for (MyMap.Entry<K,V> entry: linkedList) {
          if (entry.getKey().equals(key)) {
            return true;
          }
        }
      }

      return false;
    }

    // Returns hash of a key
    private int hash(K key) {
      return Math.abs(key.hashCode()) % size;
    }

    public static class Entry<K,V> {
      K key;
      V value;

      public Entry(K key, V value) {
        this.key = key;
        this.value = value;
      }

      public K getKey() {
        return key;
      }

      public V getValue() {
        return value;
      }

      public void setValue(V value) {
        this.value = value;
      }
    }

}

public class Solution {
  public static void main(String[] args)
    {
      MyMap<String, String> myMap = new MyMap<>(10);
      myMap.put("1", "test");
      myMap.put("1", "test2");
      myMap.put("1", "test3");
      myMap.put("2", "test4");
      myMap.put("3", "test5");
      myMap.put("2", "test6");
      System.out.println(myMap.get("1"));
      System.out.println(myMap.get("2"));
      System.out.println(myMap.get("3"));
      myMap.remove("2");
      myMap.remove(null);
      System.out.println(myMap.get("1"));
      System.out.println(myMap.get("2"));
      System.out.println(myMap.get("3"));
      System.out.println(myMap.containsKey("3"));
      System.out.println(myMap.containsKey("4"));

    }
}
