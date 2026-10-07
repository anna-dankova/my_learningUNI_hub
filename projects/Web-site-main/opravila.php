<?php include 'header.php'; ?>

<section class="container mt-5">
    <div class="card page-card glass-effect">
        <div class="page-header">
            <h1 class="mb-0">To-Do List</h1>
        </div>
        
        <div class="card-body p-5">
            <div class="input-group mb-4">
                <input type="text" id="taskInput" class="form-control" placeholder="Enter a new task...">
                <button class="btn btn-primary" id="addBtn">ADD</button>
            </div>
            
            <ul class="list-group list-group-flush" id="taskList">
            </ul>
        </div>

        <div class="card-footer bg-transparent border-0 py-4 text-center">
            <span class="text-muted">Completed: <strong id="doneCount" class="text-success">0</strong></span>
            &nbsp;&nbsp;|&nbsp;&nbsp;
            <span class="text-muted">Open: <strong id="openCount" class="text-danger">0</strong></span>
        </div>
    </div>
</section>

<?php include 'footer.php'; ?>
