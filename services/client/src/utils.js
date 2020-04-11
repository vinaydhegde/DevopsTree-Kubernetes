import axios from "axios";
//const path = `${process.env.ROOT_API}/devops`;

export const fetchTreeData = async () => {
  try {    
    const result = await axios.get('http://devops-tree/devopstree');
    return result.data;
  } catch (error) {}
};
