
import { useState, useEffect } from "react";
import axios from "axios";

const useUsers = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    
    axios.get("http://127.0.0.1:8000/api/users/")  
      .then((res) => setUsers(res.data))
      .catch((err) => console.error("Error fetching users:", err));
  }, []);

  return users;
};

export default useUsers;
