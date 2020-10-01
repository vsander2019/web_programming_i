<h3>Basic Todo List, version 1.1</h3>
<hr/>
<table border="1">
%for row in rows:
    <tr>
        <td>{{str(row[0])}}</td>
        <td>
            <a href="/update_item/{{row[0]}}">{{row[1]}}</a>
        </td>
        <td>
        %if row[2]==0:
            <a href="/set_status/{{row[0]}}/1">[ {{str(row[2])}} ]</a>
        %else:
            <a href="/set_status/{{row[0]}}/0">[ {{str(row[2])}} ]</a>
        %end
        </td>
        <td>
            <a href="/delete_item/{{row[0]}}">DELETE</a>
        </td>
    </tr>
%end
</table>
<hr/>
<<<<<<< HEAD
<a href="/new_item">New Item...</a>
=======
<a href="/new_item">New Item... :-)</a>
>>>>>>> 599f174f76b255866166ecee751681c6dffd1ce2
