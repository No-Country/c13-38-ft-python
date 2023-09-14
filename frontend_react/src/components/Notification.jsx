import React from 'react';

const Notification = ({ type, message }) => {
  let notificationClasses = 'text-sm px-4 py-2 mt-4 mb-4 rounded-md text-center';

  if (type === 'error') {
    notificationClasses += ' bg-red-500 text-white';
  } else if (type === 'success') {
    notificationClasses += ' bg-green-500 text-white';
  }

  return (
    <div className={notificationClasses}>
      {message}
    </div>
  );
};

export default Notification;