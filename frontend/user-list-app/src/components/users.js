
// import React from "react";
// import useUsers from "../hooks/useUsers";  // Import the custom hook

// const Users = () => {
//   const users = useUsers();  // Get the users data from the custom hook

//   return (
//     <div style={{ backgroundColor: "#f0f8ff", padding: "20px", borderRadius: "10px" }}>
//       <h2 style={{ color: "#333" }}>Users List</h2>
//       <ul style={{ listStyleType: "none", padding: 0 }}>
//         {users.map((user) => (
//           <li key={user.id} style={{ background: "#e6f7ff", padding: "10px", margin: "5px", borderRadius: "5px" }}>
//             <strong>{user.username}</strong> - {user.email}
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default Users;

import React, { useEffect, useState } from "react";
import axios from "axios";

const Users = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/users/")
      .then((res) => {
        console.log("API Response:", res.data); // Debugging
        setUsers(res.data.results || res.data); // Fix pagination issue
      })
      .catch((error) => console.error("Error fetching users:", error));
  }, []);

  return (
    <div style={{ backgroundColor: "#f0f8ff", padding: "20px", borderRadius: "10px" }}>
      <h2 style={{ color: "#333" }}>Users List</h2>
      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <ul style={{ listStyleType: "none", padding: 0 }}>
          {users.map((user) => (
            <li key={user.id} style={{ background: "#e6f7ff", padding: "10px", margin: "5px", borderRadius: "5px" }}>
              <strong>{user.username}</strong> - {user.email}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Users;
