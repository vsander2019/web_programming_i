<h3>Basic Todo List, version 1 testing</h3>
<hr/>
<table border="1">
%for row in rows: 
    <tr>
    %for item in row[1:]:
        <td>{{str(item)}}</td>
    %end
        <td>
            <a href="/delete_item/{{row[0]}}">DELETE</a>
        </td>
    </tr>
%end
</table>
<hr/>
<a href="/new_item">New Item...</a>
