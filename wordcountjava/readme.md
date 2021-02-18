
# About

This is a sample implementation of movie ratings inspired by [Frank's course](https://www.udemy.com/course/the-ultimate-hands-on-hadoop-tame-your-big-data/)

```bash 
mvn clean package
scp target/movierating-1.0.jar sshuser@cluster:
scp u.data sshuser@cluster:
```

When you are connected to the ssh terminal, you can run: 

```
hdfs dfs -mkdir /example/data/movie
yarn jar wordcountjava-1.0-SNAPSHOT.jar org.apache.hadoop.examples.WordCount /example/data/movie/u.data /example/data/movie
```

After the execution is finished :
```
hdfs dfs -cat /example/data/wordcountout/*
```

digital