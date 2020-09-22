<h3>Basic Todo List, version 1 testing</h3>
<hr/>
<table border="1">
%for row in rows: 
    <tr>
    %for item in row[1:]:
        <td>{{str(item)}}</td>
    %end
        <td>
<<<<<<< HEAD
          <a href="/delete_item/{{row[0]}}">DELETE</a>
=======
            <a href="/delete_item/{{row[0]}}">DELETE</a>
>>>>>>> 82ac30203eeb86aab6ffecee92e77481d307e867
        </td>
    </tr>
%end
</table>
<hr/>
<<<<<<< HEAD
<a href="/new_item">New Item...</a>
<hr/>
=======
<a href="/new_item">New Item...</a>
>>>>>>> 82ac30203eeb86aab6ffecee92e77481d307e867
