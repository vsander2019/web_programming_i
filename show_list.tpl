<html>
<head>
<title>Todo List 0.001</title>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
<link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet" >
</head>
<body>
<<<<<<< HEAD
% include("header.tpl", session=session)
<hr>
Hi, {{username}} !
<hr>
=======
%include("header.tpl", session=session)
>>>>>>> b2693012a90410afe5705293c2236191d9d3b702
<table class="w3-table w3-bordered w3-border">
%for row in rows:
    <tr>
        <td>
            <a href="/update_task/{{row['id']}}"><i class="material-icons">edit</i></a>
        </td>
        <td>
            {{row['task']}}
        </td>
        <td>
        %if row['status']==0:
            <a href="/update_status/{{row['id']}}/1"><i class="material-icons">check_box_outline_blank</i></a>
        %else:
            <a href="/update_status/{{row['id']}}/0"><i class="material-icons">check_box</i></a>
        %end
        </td>
        <td>
            <a href="/delete_item/{{row['id']}}"><i class="material-icons">delete</i></a>
        </td>
    </tr>
%end
</table>
<<<<<<< HEAD
% include("footer.tpl", session=session)
=======
%include("footer.tpl", session=session)
>>>>>>> b2693012a90410afe5705293c2236191d9d3b702
</body>
</html>